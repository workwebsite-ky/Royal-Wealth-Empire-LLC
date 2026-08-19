"""
Generates the site's abstract background artwork in the Royal Wealth Empire
brand palette (deep emerald + teal + gold), sampled directly from the client's
logo, banner and flyers:

    emerald  #042A28 / #0A2423 / #17413E
    teal     #095458 / #17828B
    gold     #B9904F / #D0A660 / #E4D0A9
    cream    #F7F2EA

Photography and flyers are the client's own files (see prep_assets.sh) —
this script only produces the gradient/texture layers behind them.
"""
import math, os, random
from PIL import Image, ImageDraw, ImageFilter, ImageChops

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "img")
os.makedirs(OUT, exist_ok=True)

INK      = (4, 14, 13)      # near-black emerald
GREEN_D  = (7, 34, 32)      # page background
GREEN_M  = (10, 42, 40)
GREEN_L  = (23, 65, 62)
TEAL_D   = (9, 84, 88)
TEAL     = (23, 130, 139)
GOLD     = (208, 166, 96)
GOLD_L   = (228, 208, 169)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def base_gradient(w, h, stops, angle=125):
    """Linear gradient across an arbitrary angle, via a 512-entry LUT."""
    img = Image.new("RGB", (w, h))
    px = img.load()
    rad = math.radians(angle)
    dx, dy = math.cos(rad), math.sin(rad)
    projs = [c[0] * dx + c[1] * dy for c in [(0, 0), (w, 0), (0, h), (w, h)]]
    lo, hi = min(projs), max(projs)
    span = (hi - lo) or 1
    lut = []
    for i in range(512):
        t = i / 511
        for j in range(len(stops) - 1):
            p0, c0 = stops[j]
            p1, c1 = stops[j + 1]
            if p0 <= t <= p1:
                lut.append(lerp(c0, c1, (t - p0) / ((p1 - p0) or 1)))
                break
        else:
            lut.append(stops[-1][1])
    for y in range(h):
        for x in range(w):
            t = ((x * dx + y * dy) - lo) / span
            px[x, y] = lut[min(511, max(0, int(t * 511)))]
    return img


def radial_glow(size, center, radius, color, strength=1.0):
    w, h = size
    layer = Image.new("RGB", (w, h), (0, 0, 0))
    d = ImageDraw.Draw(layer)
    steps = 46
    for i in range(steps, 0, -1):
        t = i / steps
        r = radius * t
        a = (1 - t) ** 2 * strength
        d.ellipse([center[0] - r, center[1] - r, center[0] + r, center[1] + r],
                  fill=tuple(int(ch * a) for ch in color))
    return layer.filter(ImageFilter.GaussianBlur(radius * 0.10))


def deco_lines(size, color=GOLD, opacity=22, spacing=54, angle=-32):
    """Thin diagonal art-deco pinstripes, echoing the flyer's gold accents."""
    w, h = size
    layer = Image.new("RGBA", (w * 2, h * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for i in range(int(w * 2 / spacing) + 2):
        x = i * spacing
        d.line([(x, 0), (x, h * 2)], fill=color + (opacity,), width=1)
    layer = layer.rotate(angle, resample=Image.BICUBIC, expand=False)
    return layer.crop((w // 2, h // 2, w // 2 + w, h // 2 + h))


def deco_arcs(size, color=GOLD, rings=7, opacity=26, cx=None, cy=None, rmax=None):
    """Concentric hairlines — a nod to the arc above the crest in the logo."""
    w, h = size
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx = w * 0.78 if cx is None else cx
    cy = h * 0.50 if cy is None else cy
    rmax = max(w, h) * 0.55 if rmax is None else rmax
    for i in range(rings):
        r = rmax * (0.35 + 0.65 * i / rings)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color + (opacity,), width=1)
    return layer


def bokeh(size, n=24, color=GOLD, seed=7, rmin=10, rmax=76, alpha=(5, 22)):
    random.seed(seed)
    w, h = size
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for _ in range(n):
        x, y = random.uniform(0, w), random.uniform(0, h)
        r = random.uniform(rmin, rmax)
        d.ellipse([x - r, y - r, x + r, y + r], fill=color + (random.randint(*alpha),))
    return layer.filter(ImageFilter.GaussianBlur(6))


def grain(img, amount=8, seed=3):
    w, h = img.size
    noise = Image.effect_noise((w, h), amount).convert("L")
    noise = noise.point(lambda v: 128 + (v - 128) * 0.45)
    return ImageChops.overlay(img, noise.convert("RGB")).convert("RGB")


def vignette(img, strength=0.7):
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).ellipse([-w * 0.25, -h * 0.35, w * 1.25, h * 1.35], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(min(w, h) * 0.16))
    return Image.composite(img, Image.blend(img, Image.new("RGB", (w, h), (0, 0, 0)),
                                            strength), mask)


def compose(name, w, h, *, stops, glows=(), seed=1, vig=0.68, quality=84,
            line_op=22, arcs=True):
    img = base_gradient(w, h, stops)
    for (cx, cy, r, col, s) in glows:
        img = ImageChops.add(img, radial_glow((w, h), (w * cx, h * cy), r, col, s))
    over = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    over = Image.alpha_composite(over, deco_lines((w, h), opacity=line_op))
    if arcs:
        over = Image.alpha_composite(over, deco_arcs((w, h)))
    over = Image.alpha_composite(over, bokeh((w, h), seed=seed))
    img = Image.alpha_composite(img.convert("RGBA"), over).convert("RGB")
    img = grain(vignette(img, vig), seed=seed)
    path = os.path.join(OUT, name)
    img.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print("%-22s %sx%s  %.1f KB" % (name, img.size[0], img.size[1],
                                    os.path.getsize(path) / 1024))


# ------------------------------------------------------------- home page hero
compose("hero-bg.jpg", 1920, 1200,
        stops=[(0.0, INK), (0.38, GREEN_D), (0.72, GREEN_L), (1.0, INK)],
        glows=[(0.74, 0.38, 640, GOLD, 0.42), (0.16, 0.74, 580, TEAL_D, 0.55)],
        seed=11)

# ----------------------------------------------------------- inner page heroes
compose("hero-services.jpg", 1600, 760,
        stops=[(0.0, INK), (0.5, GREEN_D), (1.0, GREEN_L)],
        glows=[(0.72, 0.32, 480, GOLD, 0.34), (0.2, 0.7, 420, TEAL_D, 0.45)], seed=21)

compose("hero-pricing.jpg", 1600, 760,
        stops=[(0.0, GREEN_D), (0.55, GREEN_L), (1.0, INK)],
        glows=[(0.28, 0.34, 500, GOLD, 0.32), (0.8, 0.62, 430, TEAL_D, 0.42)], seed=31)

compose("hero-about.jpg", 1600, 760,
        stops=[(0.0, INK), (0.6, GREEN_D), (1.0, GREEN_L)],
        glows=[(0.5, 0.28, 540, GOLD, 0.32), (0.12, 0.75, 400, TEAL, 0.28)], seed=41)

compose("hero-partners.jpg", 1600, 760,
        stops=[(0.0, GREEN_L), (0.5, GREEN_D), (1.0, INK)],
        glows=[(0.62, 0.42, 520, GOLD, 0.38), (0.18, 0.6, 420, TEAL_D, 0.45)], seed=51)

compose("hero-contact.jpg", 1600, 760,
        stops=[(0.0, INK), (0.5, GREEN_D), (1.0, INK)],
        glows=[(0.34, 0.4, 460, GOLD, 0.3), (0.8, 0.6, 460, TEAL_D, 0.5)], seed=61)

# ------------------------------------------------------------- texture / plate
compose("texture-deco.jpg", 1200, 900,
        stops=[(0.0, GREEN_D), (0.6, GREEN_L), (1.0, INK)],
        glows=[(0.45, 0.4, 440, GOLD, 0.34)], seed=71)
