#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Free Fire ID Checker Tool for Kali Linux
Author: HackerAI
Usage: python3 ff_checker.py <ID>
"""

import requests
import sys
import json
import argparse
from colorama import init, Fore, Style
import time

init(autoreset=True)

class FreeFireChecker:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    
    def check_id(self, player_id):
        """Multiple APIs se data fetch karta hai"""
        apis = [
            f"https://api.garena.co.id/freefire/info/{player_id}",
            f"https://free-fire-api.vercel.app/info/{player_id}",
            f"https://ff-api.glitch.me/info/{player_id}",
            f"https://api.freefire.id/player/{player_id}"
        ]
        
        for api in apis:
            try:
                print(f"{Fore.CYAN}[*] Checking: {api}")
                response = requests.get(api, headers=self.headers, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    return self.parse_data(data, player_id)
                else:
                    print(f"{Fore.RED}[!] API failed: {response.status_code}")
                    
            except Exception as e:
                print(f"{Fore.YELLOW}[!] Error: {str(e)}")
                continue
        
        return None
    
    def parse_data(self, data, player_id):
        """Data ko format karta hai"""
        result = {
            'status': False,
            'player_id': player_id,
            'name': 'Not Found',
            'level': 0,
            'rank': 'Unknown',
            'kills': 0,
            'wins': 0,
            'id_raw': data
        }
        
        # Common response formats handle karo
        try:
            if isinstance(data, dict):
                if 'name' in data:
                    result['name'] = data['name']
                    result['status'] = True
                elif 'nickname' in data:
                    result['name'] = data['nickname']
                    result['status'] = True
                elif 'playerName' in data:
                    result['name'] = data['playerName']
                    result['status'] = True
                
                result['level'] = data.get('level', result['level'])
                result['rank'] = data.get('rank', result['rank'])
                result['kills'] = data.get('kills', result['kills'])
                result['wins'] = data.get('wins', result['wins'])
        except Exception:
            pass
            
        return result
    
    def display_result(self, result):
        """Beautiful output"""
        if result and result.get('status'):
            print(f"\n{Fore.GREEN}╔════════════════════════════════════╗")
            print(f"║{'': ^40}║")
            print(f"║{Fore.YELLOW}{'✅ PLAYER FOUND!': ^36}{Style.RESET_ALL}║")
            print(f"╠════════════════════════════════════╣")
            print(f"║{Fore.CYAN}ID:{Fore.WHITE} {str(result['player_id']): ^30}║")
            print(f"║{Fore.CYAN}Name:{Fore.WHITE} {str(result['name']): ^29}║")
            print(f"║{Fore.CYAN}Level:{Fore.WHITE} {str(result['level']): ^30}║")
            print(f"║{Fore.CYAN}Rank:{Fore.WHITE} {str(result['rank']): ^29}║")
            print(f"║{Fore.CYAN}Kills:{Fore.WHITE} {str(result['kills']): ^29}║")
            print(f"║{Fore.CYAN}Wins:{Fore.WHITE} {str(result['wins']): ^29}║")
            print(f"╚════════════════════════════════════╝{Style.RESET_ALL}")
        else:
            pid = result['player_id'] if result and 'player_id' in result else 'Unknown'
            print(f"\n{Fore.RED}❌ Player ID {pid} not found!")
            print(f"{Fore.YELLOW}[!] Try valid Free Fire ID (8-12 digits)")
            
def banner():
    print(f\"\"\" 
{Fore.RED}╔══════════════════════════════════════╗
║{Fore.YELLOW}    Free Fire ID Checker v2.0     {Fore.RED}║
║{Fore.WHITE}     Kali Linux Tool 2026       {Fore.RED}║
╚══════════════════════════════════════╝{Style.RESET_ALL}
    \"\"\")
    
def main():
    banner()
    
    parser = argparse.ArgumentParser(description='Free Fire ID Checker')
    parser.add_argument('id', nargs='?', help='Free Fire Player ID')
    parser.add_argument('-b', '--batch', help='Batch file with IDs')
    
    args = parser.parse_args()
    
    if not args.id and not args.batch:
        print(f\"{Fore.YELLOW}Usage: python3 ff_checker.py <ID>\")
        print(f\"Example: python3 ff_checker.py 12345678\")
        sys.exit(1)
    
    checker = FreeFireChecker()
    
    if args.batch:
        # Batch mode
        try:
            with open(args.batch, 'r') as f:
                ids = [line.strip() for line in f if line.strip()]
            
            print(f\"{Fore.CYAN}[*] Loading {len(ids)} IDs from batch file\")
            
            for i, player_id in enumerate(ids, 1):
                print(f\"\\n{Fore.MAGENTA}[{i}/{len(ids)}]{Style.RESET_ALL}\")
                result = checker.check_id(player_id)
                checker.display_result(result)
                time.sleep(1)
                
        except FileNotFoundError:
            print(f\"{Fore.RED}[!] Batch file not found: {args.batch}\")
    else:
        # Single ID
        result = checker.check_id(args.id)
        checker.display_result(result)

if __name__ == \"__main__\":
    main()
