from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os
import sqlite3
import os

app = Flask(__name__)

# Create DB on first run
conn = sqlite3.connect("links.db")
conn.execute("CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY, url TEXT)")
conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]

        # Ensure the URL starts with http:// or https://
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        conn = sqlite3.connect("links.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO links (url) VALUES (?)", (url,))
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()

        # Update the QR URL based on ngrok
        qr_url = f"https://6a29-39-61-32-75.ngrok-free.app/q/{new_id}"
        img = qrcode.make(qr_url)
        img.save(f"static/qrcode_{new_id}.png")

        return render_template("result.html", qr_id=new_id, qr_path=f"/static/qrcode_{new_id}.png")

    return render_template("index.html")


@app.route("/q/<int:qr_id>")
def dynamic_redirect(qr_id):
    conn = sqlite3.connect("links.db")
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM links WHERE id = ?", (qr_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return redirect(row[0])
    else:
        return "Invalid QR code", 404

@app.route("/edit/<int:qr_id>", methods=["GET", "POST"])
def edit(qr_id):
    conn = sqlite3.connect("links.db")
    cursor = conn.cursor()

    if request.method == "POST":
        new_url = request.form["url"]

        # Ensure the URL starts with http:// or https://
        if not new_url.startswith("http://") and not new_url.startswith("https://"):
            new_url = "http://" + new_url

        cursor.execute("UPDATE links SET url = ? WHERE id = ?", (new_url, qr_id))
        conn.commit()
        conn.close()

        # Redirect to result page to view QR again
        return redirect(f"/q/{qr_id}")

    cursor.execute("SELECT url FROM links WHERE id = ?", (qr_id,))
    row = cursor.fetchone()
    conn.close()

    return render_template("edit.html", qr_id=qr_id, current_url=row[0] if row else "")


if __name__ == "__main__":
    app.run(debug=True)

