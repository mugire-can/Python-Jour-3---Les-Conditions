#!/usr/bin/env python3
"""Main entry point for Python Day 3 exercises.

Interactive menu system to run individual exercises or all at once.
"""

import time
from typing import Callable
from jobs import JOBS
from config import SHOW_TIMING


def display_banner() -> None:
    """Display welcome banner."""
    print("\n" + "="*60)
    print("  PYTHON DAY 3 - CONDITIONAL STATEMENTS EXERCISES")
    print("="*60 + "\n")


def display_menu() -> None:
    """Display main menu options."""
    print("\n📋 MENU - Sélectionnez un exercice:")
    print("-" * 60)
    for key, (description, _) in JOBS.items():
        print(f"  {key}. {description}")
    print("  9. Exécuter tous les exercices")
    print("  0. Quitter")
    print("-" * 60)


def run_job(key: str, job_func: Callable) -> None:
    """Execute a single job with optional timing.
    
    Args:
        key: Job identifier.
        job_func: Function to execute.
    """
    print(f"\n{'='*60}")
    print(f"🎯 JOB {key}: {JOBS[key][0]}")
    print('='*60)
    
    if SHOW_TIMING:
        start = time.time()
    
    try:
        job_func()
    except KeyboardInterrupt:
        print("\n⚠ Exercice annulé par l'utilisateur")
    except Exception as e:
        print(f"⚠ Erreur lors de l'exécution: {e}")
    
    if SHOW_TIMING:
        elapsed = time.time() - start
        print(f"⏱ Temps d'exécution: {elapsed:.3f}s")


def run_all_jobs() -> None:
    """Execute all jobs in sequence."""
    print("\n🚀 Exécution de tous les exercices...")
    for key in sorted(JOBS.keys()):
        run_job(key, JOBS[key][1])
    print("\n✓ Tous les exercices sont terminés!")


def main() -> None:
    """Main interactive menu loop."""
    display_banner()
    
    while True:
        display_menu()
        choice = input("\n👉 Entrez votre choix: ").strip()
        
        if choice == "0":
            print("\n👋 Au revoir!")
            break
        elif choice == "9":
            run_all_jobs()
        elif choice in JOBS:
            run_job(choice, JOBS[choice][1])
        else:
            print("⚠ Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
