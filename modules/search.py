from typing import List, Dict


def find_pattern(pattern: str, documents: List[str])->List[Dict[str, str]]:
    results = []
    for f in documents:
        with open(f'notes/{f}') as file:
            for line_no, line in enumerate(file):
                if line.find(pattern) > -1:
                    result = {
                        'pattern': pattern,
                        'line_no': str(line_no),
                        'line': line,
                        'document': f
                    }
                    results.append(result)
    return results
