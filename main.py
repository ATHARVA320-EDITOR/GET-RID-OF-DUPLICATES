student_data = {'id1':
     {'Name': ['Sara'],
      'class': ['V'],
      'subject_integration': ['English, Math, Science']
     },
     'id2' :
      {'Name': ['David'],
      'class': ['V'],
      'subject_integration': ['English, Math, Science']
     },
     'id3':
      {'Name': ['Sara'],
      'class': ['V'],
      'subject_integration': ['English, Math, Science']
     },
     'id4':
      {'Name': ['Surya'],
      'class': ['V'],
      'subject_integration': ['English, Math, Science']
     },
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)