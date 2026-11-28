# Security headers (set in Cloudflare)

GitHub Pages cannot send custom headers, so these are set in the Cloudflare dashboard:
choose quirinalstudios.com, then Rules, create a response header transform rule that applies
to all incoming requests, and add each header with "Set static".

| Header name | Value |
|---|---|
| `X-Content-Type-Options` | `nosniff` |
| `X-Frame-Options` | `DENY` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Content-Security-Policy-Report-Only` | see below |

Content-Security-Policy-Report-Only value, one line:

```
default-src 'self'; script-src 'self' https://esm.sh 'sha256-WuIl+kdB5bYd5bsPGcsfjKGbEenw8bfDCUrK1uAOCL8=' 'sha256-oGwnBxWHqtWAcK3+qW3A2rs/Fc71IM9SD9XJhWPwpbM=' 'sha256-QoPLR3bIuPeBRlYOdUFdKWYeUQqEQh60KfBT+ZdA1qg=' 'sha256-QBL8mpYnOmRLeVyXmm3pmzzhAFap6z+yE142zIcxGUo='; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https://ipip.fyi; connect-src 'self' https://in.heycatch.ai; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'
```

## Tightening the policy

Report-Only blocks nothing. No reporting address is configured, so violations appear only in a
browser's developer console. Browsers also ignore `frame-ancestors` in a report-only policy
(`X-Frame-Options` covers framing meanwhile).

After a week, open the main pages, both before and after choosing Allow on the analytics banner,
and check the console. If nothing is reported, rename the header to `Content-Security-Policy`.

## Update the policy when

- a page gains a script, style, font or image from a new outside address;
- a short-link redirect page's inline script changes (its `sha256-` value must be recalculated).
