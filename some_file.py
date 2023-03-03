data1 = ['Commands', 'Documents', 'WorkSpace', 'React', 'Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified', 'General', 'Word File.doc']
data2 = ['commands', 'documents', 'workspace', 'react', 'angular', 'veu', 'office', 'public', 'private', 'classified', 'general', 'wordFile']
# data2 = ['Commands', 'Documents', 'WorkSpace', 'React', 'Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified', 'General', 'Word File.doc']

print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())
print(data2)

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ', '').lower()
assert data1 == data2
