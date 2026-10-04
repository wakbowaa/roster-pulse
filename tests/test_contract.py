from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text(encoding='utf-8')
def test_public_surface():
 for name in ['create_roster','post_task','accept_task','decline_task','expire_assignment','complete_task','get_roster']:assert f'def {name}' in S
def test_consensus_binds_eligibility():
 for value in ['eligible_indexes','coverage for every member','complete eligible index set','run_nondet_unsafe']:assert value in S
def test_fair_and_recoverable_assignment():
 for value in ["key=lambda i:(counts[i],i)",'expired assignment','UNFILLED','ACCEPTED','COMPLETED']:assert value in S
def test_pinned_runner():assert S.startswith('# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }')
