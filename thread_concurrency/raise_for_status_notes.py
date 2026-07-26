"""
===========================================================
        response.raise_for_status()
===========================================================

What is it?

Hinglish
---------

response.raise_for_status()

HTTP response ko check karta hai.

Agar response successful hai

(200-299)

to kuch nahi hota.

Agar response fail ho jaye

(404, 500, 403...)

to HTTPError raise karta hai.

-----------------------------------------------------------

English
--------

Checks whether the HTTP request
was successful.

If successful,

continues execution.

Otherwise,

raises an HTTPError.

-----------------------------------------------------------

Without raise_for_status()

Server returns

404

↓

Program still continues.

May save invalid data.

-----------------------------------------------------------

With raise_for_status()

Server returns

404

↓

Raises HTTPError

↓

Program goes to except block.

-----------------------------------------------------------

Best Practice

response = requests.get(url, timeout=10)

response.raise_for_status()

-----------------------------------------------------------

Common Status Codes

200 → OK

201 → Created

204 → No Content

400 → Bad Request

401 → Unauthorized

403 → Forbidden

404 → Not Found

500 → Internal Server Error

503 → Service Unavailable

-----------------------------------------------------------

Golden Rule

Always call

response.raise_for_status()

after

requests.get()

to detect HTTP errors early.

===========================================================
"""