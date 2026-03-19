import json

with open('test_systems.json', 'r') as f:
    systems = json.load(f)

print(f'Total systems in test_systems.json: {len(systems)}')
print('\nSystem names and expected classifications:')
for i, sys in enumerate(systems, 1):
    print(f'{i}. {sys["name"]} -> {sys.get("expected_classification", "UNKNOWN")}')
