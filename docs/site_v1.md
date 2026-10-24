# foodporter.nl site v1 — 2026-10-24
Repo: github.com/bazsozsolt/foodporter-site (main = source, gh-pages = `site/`, deploy: `python3 src/build.py && git subtree push --prefix site origin gh-pages`). GitHub Actions workflow not used (gh token lacks `workflow` scope).
Pages settings: custom domain foodporter.nl, cert approved (foodporter.nl + www, exp 2027-01-22), HTTPS enforced.
## Built
- Static generator src/build.py (NL+EN content side by side, guaranteed parity), plain CSS, no JS except 404 forwarder, no cookies/tracking.
- 8 pages × 2 langs: home, klanten/customers, restaurants, bezorgers/riders, over-ons/about, veelgestelde-vragen/faq, contact, juridisch/legal. Lang switch to counterpart page, hreflang, canonical, OG + og.png 1200×630, sitemap.xml, robots.txt, favicon, 404.
- Legal links → app.foodporter.nl /privacy /terms /cookies /accessibility, marked draft pending Dutch lawyer review.
- Rider bonus kept generic (amount set in admin; shown in contract/rider app). Restaurant sign-up = mailto partners@ + restaurant sign-in in app (app has no self-service restaurant onboarding).
- Placeholders (yellow dashed): KvK, VAT, address.
- Old link fallback: /foodporter-app/* and app routes (/login/, /order/ …) on foodporter.nl forward to app.foodporter.nl. GitHub currently 301s bazsozsolt.github.io/foodporter-app/X → foodporter.nl/X, so this is needed.
## Checks
- Chrome (one browser): all 16 pages 200, no console errors, no horizontal overflow at 1366 and 390 px.
- Redirects: /foodporter-app/ → app root, /foodporter-app/login/ → app /login/, /login/ → app /login/, unknown → 404.
- App links 200 (/, /restaurant/, /rider-info/, /privacy/, /terms/, /cookies/, /accessibility/).
- Lighthouse 12 (local): home and restaurants 100/100/100/100.
## OPEN — DNS (Zsolt)
TransIP's authoritative NS currently answer apex A = 37.97.254.27 (parking) again; www CNAME = foodporter.nl. Some resolvers still show GitHub IPs from cache, so visitors randomly get parking. Fix in TransIP: delete A 37.97.254.27 for @, keep 4× 185.199.10x.153, set www CNAME bazsozsolt.github.io., save. Then recheck http→https and www→apex (box can't test plain http).
Screenshots: /workspace/screens_site_v1/{desktop,mobile}_nl_*.png
