'''Faça um programa que cadastre n alunos. Para cada aluno devem ser cadastrados
nome e nota final. Os dados devem ser armazenados em uma lista duplamente
encadeada e não ordenada. Em seguida, o programa deve mostrar apenas o nome
dos alunos aprovados, ou seja, alunos com nota final de no mínimo 7. Se nenhum
aluno estiver aprovado, mostrar mensagem.'''

from doublyCircularLinkedUnorderedList import DoublyCircularLinkedUnorderedList

def verifiedInput(type, message):
    try:
        return type(input(message))
    except:
        print('Valor inválido!')
        verifiedInput(type, message)

def approvedStudents(students: DoublyCircularLinkedUnorderedList):
    approved_students = []
    
    if students.head.data['final_grade'] >= 7.0:
        approved_students.append(students.head.data['name'])
    
    current = students.head.next
    while current != students.head:
        if current.data['final_grade'] >= 7.0:
            approved_students.append(current.data['name'])
        current = current.next
    return approved_students

def show_results(approved_students: list):
    print()
    if len(approved_students) == 0:
        print('Nenhum aluno aprovado!')
    else:
        for student in approved_students:
            print(f'O aluno {student} foi aprovado.')

def main():
    students = DoublyCircularLinkedUnorderedList()
    
    answer = 's'
    while answer != 'n':
        name = verifiedInput(str, 'Digite o nome do aluno: ')
        final_grade = verifiedInput(float, 'Digite a nota final do aluno: ')
        students.insert_front({'name': name, 'final_grade': final_grade})
        
        answer = input('Deseja continuar? (s/n)').lower().strip()
        
    approved_students = approvedStudents(students)
    show_results(approved_students)

main()