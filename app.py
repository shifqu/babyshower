import os
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
DB = os.environ.get("DB_PATH", os.path.join(os.path.dirname(__file__), "responses.db"))


def init_db():
    db_dir = os.path.dirname(DB)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS responses (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                naam            TEXT NOT NULL,
                geboortedag     TEXT,
                geboortemaand   TEXT,
                geboortetijd    TEXT,
                jongen_meisje   TEXT,
                gewicht         TEXT,
                lengte          TEXT,
                kleur_haar      TEXT,
                kleur_ogen      TEXT,
                lijkt_op        TEXT,
                tips            TEXT,
                q1  TEXT, q2  TEXT, q3  TEXT, q4  TEXT, q5  TEXT,
                q6  TEXT, q7  TEXT, q8  TEXT, q9  TEXT, q10 TEXT,
                q11 TEXT, q12 TEXT, q13 TEXT, q14 TEXT, q15 TEXT,
                ingediend_op    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    f = request.form
    with sqlite3.connect(DB) as conn:
        conn.execute(
            """
            INSERT INTO responses (
                naam, geboortedag, geboortemaand, geboortetijd, jongen_meisje,
                gewicht, lengte, kleur_haar, kleur_ogen, lijkt_op, tips,
                q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                f.get("naam"),
                f.get("geboortedag"),
                f.get("geboortemaand"),
                f.get("geboortetijd"),
                f.get("jongen_meisje"),
                f.get("gewicht"),
                f.get("lengte"),
                f.get("kleur_haar"),
                f.get("kleur_ogen"),
                f.get("lijkt_op"),
                f.get("tips"),
                f.get("q1"),
                f.get("q2"),
                f.get("q3"),
                f.get("q4"),
                f.get("q5"),
                f.get("q6"),
                f.get("q7"),
                f.get("q8"),
                f.get("q9"),
                f.get("q10"),
                f.get("q11"),
                f.get("q12"),
                f.get("q13"),
                f.get("q14"),
                f.get("q15"),
            ),
        )
    return render_template("thanks.html", naam=f.get("naam", "Gast"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
