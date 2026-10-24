# foodporter.nl site v2 — live check 2026-10-24 (14:52–14:55 Amsterdam)
- DNS (dns.google) start + end: apex A 185.199.108-111.153, www + app CNAME bazsozsolt.github.io. — no reversion to 37.97.254.27.
- HTTPS: cert foodporter.nl + www.foodporter.nl, valid to 2027-01-22. www → 301 apex.
- All 16 sitemap pages (NL+EN) 200 on desktop 1366 and mobile 390: no console errors, no horizontal overflow, language switch present on each.
- 46 unique links (incl. into app) all 200. sitemap.xml + robots.txt 200, unknown URL → 404.
- Forwarders: /foodporter-app/, /foodporter-app/login/, /login/, /order/ → app.foodporter.nl equivalents.
- Lighthouse 12 live home: mobile 100/100/100/100, desktop 99/100/100/100.
- No bugs found. Still open: KvK, VAT, address placeholders; confirm partners@foodporter.nl (mailbox needs Brevo/mail setup).
