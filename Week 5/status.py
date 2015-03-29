def status_count(students):

    result = {
        'finalized': [],
        'not_finalized': []
        }

    for a in students:

        if a['status'] == 'finalized':  # dali st-ta na klu4 'status' e 'finalized'
            result['finalized'] += [a['name']]

# result['finalized'].append(a['name']) - 2ri na4in za dobavqne na str kym spisyka result['finalized']
        elif a['status'] == 'not_finalized':
            result['not_finalized'] += [a['name']]

    return result

print(status_count([
    {"name": "RadoRado", "status": "not_finalized"},
    {"name": "Ivo", "status": "finalized"},
    {"name": "Genadi", "status": "finalized"}
    ]))
