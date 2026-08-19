/* ==========================================================================
   ROYAL WEALTH EMPIRE LLC — main.js
   Vanilla JS. No dependencies. Progressive-enhancement friendly.
   --------------------------------------------------------------------------
   1.  Preloader
   2.  Sticky header
   3.  Mobile menu
   4.  Active nav link
   5.  Scroll reveal (IntersectionObserver)
   6.  Animated counters
   7.  Hero parallax
   8.  Card spotlight (cursor-follow glow)
   9.  FAQ accordion
   10. Testimonial slider
   11. Back-to-top
   12. Contact form (mailto fallback)
   13. Footer year
   ========================================================================== */
(function () {
  "use strict";

  const $ = (s, ctx = document) => ctx.querySelector(s);
  const $$ = (s, ctx = document) => Array.from(ctx.querySelectorAll(s));
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------------- 1. Preloader */
  const preloader = $("#preloader");
  if (preloader) {
    const hide = () => setTimeout(() => preloader.classList.add("done"), 380);
    window.addEventListener("load", hide);
    // Safety net so the page is never stuck behind the loader
    setTimeout(hide, 3500);
  }

  /* ------------------------------------------------------------ 2. Sticky header */
  const header = $(".site-header");
  const onScroll = () => {
    if (header) header.classList.toggle("scrolled", window.scrollY > 40);
    const top = $("#toTop");
    if (top) top.classList.toggle("show", window.scrollY > 520);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* -------------------------------------------------------------- 3. Mobile menu */
  const toggle = $(".nav-toggle");
  const drawer = $(".mobile-menu");
  if (toggle && drawer) {
    const setOpen = (open) => {
      toggle.classList.toggle("open", open);
      drawer.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    };
    toggle.addEventListener("click", () => setOpen(!drawer.classList.contains("open")));
    $$("a", drawer).forEach((a) => a.addEventListener("click", () => setOpen(false)));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") setOpen(false);
    });
  }

  /* ---------------------------------------------------------- 4. Active nav link */
  const here = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  $$(".nav-menu a, .mobile-menu a").forEach((a) => {
    const href = (a.getAttribute("href") || "").split("#")[0].toLowerCase();
    if (href && href === here) a.classList.add("active");
  });

  /* ------------------------------------------------------------ 5. Scroll reveal */
  const revealables = $$("[data-reveal]");
  if (revealables.length) {
    if (reduced || !("IntersectionObserver" in window)) {
      revealables.forEach((el) => el.classList.add("in"));
    } else {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            const el = entry.target;
            const delay = parseInt(el.dataset.delay || "0", 10);
            setTimeout(() => el.classList.add("in"), delay);
            io.unobserve(el);
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -70px 0px" }
      );
      revealables.forEach((el) => io.observe(el));
    }
  }

  /* -------------------------------------------------------- 6. Animated counters */
  const counters = $$("[data-count]");
  if (counters.length) {
    const run = (el) => {
      const target = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || "";
      const decimals = (el.dataset.decimals | 0);
      const dur = 1600;
      const start = performance.now();
      const tick = (now) => {
        const p = Math.min((now - start) / dur, 1);
        const eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
        el.textContent = (target * eased).toFixed(decimals) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    if (reduced || !("IntersectionObserver" in window)) {
      counters.forEach((el) => (el.textContent = el.dataset.count + (el.dataset.suffix || "")));
    } else {
      const co = new IntersectionObserver(
        (entries) => {
          entries.forEach((e) => {
            if (e.isIntersecting) {
              run(e.target);
              co.unobserve(e.target);
            }
          });
        },
        { threshold: 0.5 }
      );
      counters.forEach((el) => co.observe(el));
    }
  }

  /* ----------------------------------------------------------- 7. Hero parallax */
  const heroBg = $(".hero-bg");
  if (heroBg && !reduced) {
    let ticking = false;
    window.addEventListener(
      "scroll",
      () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => {
          const y = window.scrollY;
          if (y < window.innerHeight * 1.2) {
            heroBg.style.transform = `scale(1.08) translate3d(0, ${y * 0.18}px, 0)`;
          }
          ticking = false;
        });
      },
      { passive: true }
    );
  }

  /* ------------------------------------------------------- 8. Card spotlight glow */
  if (!reduced && window.matchMedia("(hover: hover)").matches) {
    $$(".card").forEach((card) => {
      card.addEventListener("mousemove", (e) => {
        const r = card.getBoundingClientRect();
        card.style.setProperty("--mx", `${e.clientX - r.left}px`);
        card.style.setProperty("--my", `${e.clientY - r.top}px`);
      });
    });
  }

  /* ----------------------------------------------------------- 9. FAQ accordion */
  $$(".faq-item").forEach((item) => {
    const q = $(".faq-q", item);
    const a = $(".faq-a", item);
    if (!q || !a) return;
    q.addEventListener("click", () => {
      const isOpen = item.classList.contains("open");
      // close siblings for a clean single-open accordion
      const parent = item.parentElement;
      $$(".faq-item.open", parent).forEach((other) => {
        other.classList.remove("open");
        $(".faq-q", other).setAttribute("aria-expanded", "false");
        $(".faq-a", other).style.maxHeight = null;
      });
      if (!isOpen) {
        item.classList.add("open");
        q.setAttribute("aria-expanded", "true");
        a.style.maxHeight = a.scrollHeight + "px";
      }
    });
  });

  /* ------------------------------------------------------ 10. Testimonial slider */
  const slider = $("[data-slider]");
  if (slider) {
    const slides = $$(".testi-slide", slider);
    const dotsWrap = $("[data-slider-dots]");
    let index = 0;
    let timer;

    const show = (i) => {
      index = (i + slides.length) % slides.length;
      slides.forEach((s, n) => {
        s.style.display = n === index ? "" : "none";
        if (n === index) {
          s.classList.remove("in");
          void s.offsetWidth; // restart animation
          s.classList.add("in");
        }
      });
      if (dotsWrap) {
        $$("button", dotsWrap).forEach((d, n) => {
          d.style.background = n === index ? "#D4AF37" : "rgba(255,255,255,.2)";
          d.style.width = n === index ? "26px" : "9px";
        });
      }
    };

    if (dotsWrap) {
      slides.forEach((_, n) => {
        const b = document.createElement("button");
        b.type = "button";
        b.setAttribute("aria-label", "Go to testimonial " + (n + 1));
        b.style.cssText =
          "height:9px;width:9px;border-radius:999px;background:rgba(255,255,255,.2);transition:all .4s cubic-bezier(.22,1,.36,1);cursor:pointer;";
        b.addEventListener("click", () => {
          show(n);
          restart();
        });
        dotsWrap.appendChild(b);
      });
    }

    const next = () => show(index + 1);
    const restart = () => {
      clearInterval(timer);
      if (!reduced) timer = setInterval(next, 6500);
    };

    $$("[data-slider-prev]").forEach((b) => b.addEventListener("click", () => { show(index - 1); restart(); }));
    $$("[data-slider-next]").forEach((b) => b.addEventListener("click", () => { next(); restart(); }));

    show(0);
    restart();
    slider.addEventListener("mouseenter", () => clearInterval(timer));
    slider.addEventListener("mouseleave", restart);
  }

  /* ------------------------------------------------------------ 11. Back to top */
  const toTop = $("#toTop");
  if (toTop) {
    toTop.addEventListener("click", () =>
      window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" })
    );
  }

  /* --------------------------------------------------------- 12. Contact form
     No backend is required: the form composes a pre-filled email and opens the
     visitor's mail client addressed to the business. Swap the `action` for a
     Formspree/Netlify endpoint later if you want inbox delivery without mailto.
  ---------------------------------------------------------------------------- */
  $$("[data-mailto-form]").forEach((form) => {
    const status = $(".form-status", form);
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const to = form.dataset.mailtoForm || "Theroyalwealthempire@gmail.com";
      const name = (data.get("name") || "").toString().trim();
      const subject = encodeURIComponent(
        (form.dataset.subject || "New Website Enquiry") + (name ? " — " + name : "")
      );
      const lines = [];
      for (const [key, value] of data.entries()) {
        if (!value) continue;
        const label = key.replace(/[-_]/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
        lines.push(label + ": " + value);
      }
      lines.push("", "— Sent from royalwealthempire.com");
      const body = encodeURIComponent(lines.join("\n"));

      window.location.href = `mailto:${to}?subject=${subject}&body=${body}`;

      if (status) {
        status.textContent =
          "Opening your email app… If nothing happens, email us directly at " + to;
        status.classList.add("show");
      }
      form.reset();
    });
  });

  /* ------------------------------------------------------------- 13. Year stamp */
  $$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));
})();
