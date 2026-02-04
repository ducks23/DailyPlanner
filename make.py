import os
import shutil
from datetime import date, timedelta


def generate_daily_planner(
    template_path: str,
    output_dir: str,
    start_date: date,
    end_date: date
):
    """
    Generate daily planner markdown files from template.

    Args:
        template_path: Path to markdown template
        output_dir: Root planner directory
        start_date: Start date
        end_date: End date
    """

    if not os.path.exists(template_path):
        raise FileNotFoundError("Template file not found")

    current = start_date

    while current <= end_date:

        year = current.strftime("%Y")
        month = current.strftime("%m")
        filename = current.strftime("%Y-%m-%d.md")

        # Create directory structure
        day_dir = os.path.join(output_dir, year, month)
        os.makedirs(day_dir, exist_ok=True)

        output_file = os.path.join(day_dir, filename)

        # Copy template and replace date placeholder
        with open(template_path, "r") as template:
            content = template.read()

        content = content.replace("{{DATE}}", current.strftime("%A, %B %d, %Y"))

        with open(output_file, "w") as f:
            f.write(content)

        current += timedelta(days=1)


# Example Usage
if __name__ == "__main__":

    generate_daily_planner(
        template_path="daily_template.md",
        output_dir="planner",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31)
    )
