import re
import sys

def convert_mysql_to_postgres(sql: str) -> str:
    # Remove backticks
    sql = sql.replace("`", "")

    # Replace AUTO_INCREMENT with SERIAL
    sql = re.sub(r"\bint NOT NULL AUTO_INCREMENT\b", "SERIAL PRIMARY KEY", sql, flags=re.IGNORECASE)

    # Remove ENGINE, CHARSET, COLLATE clauses
    sql = re.sub(r"ENGINE=\w+\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"DEFAULT CHARSET=\w+\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"COLLATE=\w+\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"AUTO_INCREMENT=\d+\s*", "", sql, flags=re.IGNORECASE)

    # Remove redundant PRIMARY KEY lines if SERIAL PRIMARY KEY already exists
    sql = re.sub(r",?\s*PRIMARY KEY\s*\([^)]+\)", "", sql, flags=re.IGNORECASE)

    # Remove MySQL KEY definitions (indexes) inside CREATE TABLE
    sql = re.sub(r",?\s*KEY\s+\w+\s*\([^)]+\)", "", sql, flags=re.IGNORECASE)

    # Remove stray MySQL artifacts like ENGINE, AUTO_INCREMENT, or dangling characters
    sql = re.sub(r";\s*s", ";", sql, flags=re.IGNORECASE)  # remove ';s' errors
    sql = re.sub(r"\)\s*;s", ");", sql, flags=re.IGNORECASE)

    # Remove MySQL-specific column attributes
    sql = re.sub(r"\bUNSIGNED\b", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"ON UPDATE CURRENT_TIMESTAMP", "", sql, flags=re.IGNORECASE)

    # Remove MySQL-style comments
    sql = re.sub(r"--.*", "", sql)
    sql = re.sub(r"/\*.*?\*/", "", sql, flags=re.DOTALL)

    # Remove MySQL table options after closing parenthesis
    sql = re.sub(r"\)\s*ENGINE.*?;", ");", sql, flags=re.IGNORECASE)
    sql = re.sub(r"\)\s*AUTO_INCREMENT.*?;", ");", sql, flags=re.IGNORECASE)
    sql = re.sub(r"\)\s*DEFAULT CHARSET.*?;", ");", sql, flags=re.IGNORECASE)

    # Clean up multiple spaces and newlines
    sql = re.sub(r"\n\s*\n", "\n", sql)
    sql = re.sub(r"\s{2,}", " ", sql)

    return sql.strip()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_sql.py input.sql output.sql")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    with open(input_file, "r") as f:
        mysql_sql = f.read()

    postgres_sql = convert_mysql_to_postgres(mysql_sql)

    with open(output_file, "w") as f:
        f.write(postgres_sql)

    print(f"Converted SQL written to {output_file}")
