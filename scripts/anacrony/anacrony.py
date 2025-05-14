#!/usr/bin/env python3

import subprocess
import questionary
from rich.console import Console
from rich.table import Table
from rich import box
import re
import os

console = Console()
ANACRONTAB = "/etc/anacrontab"

def check_root():
    if os.geteuid() != 0:
        console.print("[red]Please run this script with sudo.[/red]")
        exit(1)

def list_jobs():
    table = Table(title="Anacron Jobs", box=box.SIMPLE_HEAVY)
    table.add_column("Period (days)", justify="center")
    table.add_column("Delay (minutes)", justify="center")
    table.add_column("Job", style="cyan")
    table.add_column("Command", style="green")

    with open(ANACRONTAB, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() and not line.startswith("#"):
                parts = line.strip().split(None, 3)
                if len(parts) == 4:
                    table.add_row(*parts)

    console.print(table)

def add_job():
    job = questionary.text("Job name (no spaces):").ask()
    period = questionary.text("Period in days (e.g. 1 for daily, 7 for weekly):").ask()
    delay = questionary.text("Delay in minutes before running (0 for immediate):").ask()
    cmd = questionary.text("Command to run:").ask()

    line = f"{period} {delay} {job} {cmd}\n"

    with open(ANACRONTAB, "a") as f:
        f.write(line)

    console.print(f"[green]Job '{job}' added successfully.[/green]")

def remove_job():
    with open(ANACRONTAB, "r") as f:
        lines = f.readlines()

    jobs = [line for line in lines if line.strip() and not line.startswith("#")]

    job_names = [line.split()[2] for line in jobs if len(line.split()) >= 3]
    if not job_names:
        console.print("[yellow]No jobs to remove.[/yellow]")
        return

    job_to_remove = questionary.select("Select job to remove:", choices=job_names).ask()
    new_lines = [line for line in lines if not (line.strip() and line.split()[2] == job_to_remove)]

    with open(ANACRONTAB, "w") as f:
        f.writelines(new_lines)

    console.print(f"[red]Job '{job_to_remove}' removed.[/red]")

def monitor_logs():
    console.print("[bold cyan]Recent Anacron log entries:[/bold cyan]")
    try:
        result = subprocess.run(["journalctl", "-u", "anacron", "-n", "20", "--no-pager"], capture_output=True, text=True)
        console.print(result.stdout)
    except Exception:
        console.print("[red]Could not retrieve logs from journalctl. Falling back to /var/log/syslog.[/red]")
        subprocess.run("grep anacron /var/log/syslog | tail -n 20", shell=True)

def main():
    check_root()

    while True:
        action = questionary.select(
            "What do you want to do?",
            choices=[
                "📋 List jobs",
                "➕ Add a job",
                "❌ Remove a job",
                "📊 Monitor recent logs",
                "🚪 Exit"
            ]
        ).ask()

        if action == "📋 List jobs":
            list_jobs()
        elif action == "➕ Add a job":
            add_job()
        elif action == "❌ Remove a job":
            remove_job()
        elif action == "📊 Monitor recent logs":
            monitor_logs()
        elif action == "🚪 Exit":
            break

if __name__ == "__main__":
    main()

