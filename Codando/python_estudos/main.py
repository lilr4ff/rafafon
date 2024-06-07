import streamlit as st
from user_management import UserManagement
from data_service import Horariomarcado
from streamlit_option_menu import option_menu

page_config = st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    selected = option_menu("Main Menu", ["Adicionar usuário", "Atualizar usuário", "Listar usuários", "Marcar horário"])

'''
menu = ["Adicionar usuário", "Atualizar usuário", "Listar usuários", "Marcar horário"]
escolha = st.sidebar.selectbox("Menu", menu)
'''

if escolha == "Adicionar usuário":

    with st.form(key='add_user_form'):
        st.subheader("Dados de usuário")
        cpf = st.text_input('CPF')
        nome = st.text_input('Nome')
        celular = st.text_input('Celular')
        email = st.text_input('Email')
        st.divider()
        
        st.subheader("Endereço da visita")
        cep = st.text_input('CEP')
        rua = st.text_input('Rua')
        bairro = st.text_input('Bairro')
        numero = st.text_input('Número')
        submit_button = st.form_submit_button(label='Agendar visita')
        if submit_button:
            resultado = controlador.add_user(cpf, nome, celular, email, cep, rua, bairro, numero)
            st.success(resultado)

elif escolha == "Atualizar usuário":
    st.subheader("Atualizar dados de usuário")
    cpf = st.text_input('Insira o CPF do usuário a ser atualizado')
    user = controlador.usuario_por_cpf(cpf)
    
    if user:
        with st.form(key='update_user_form'):
            nome = st.text_input('Novo nome', user['nome'])
            celular = st.text_input('Novo celular', user['celular'])
            email = st.text_input('Novo e-mail', user['email'])
            cep = st.text_input('Novo CEP', user['cep'])
            rua = st.text_input('Novo Logradouro', user['rua'])
            bairro = st.text_input('Novo Bairro', user['bairro'])
            numero = st.text_input('Novo número', user['numero'])
            submit_button = st.form_submit_button(label='Atualizar')
            
            if submit_button:
                resultado = controlador.atualizar_user(cpf, nome, celular, email, cep, rua, bairro, numero)
                st.success(resultado)
    else:
        st.error('Usuário não encontrado')

elif escolha == "Listar usuários":
    st.subheader("Lista de usuários cadastrados")
    usuarios = controlador.listar_usuarios()
    if usuarios:
        for user in usuarios:
            st.write(user)
    else:
        st.write('Nenhum usuário cadastrado.')

elif escolha == "Marcar horário":
    st.subheader("Marcar horário para um serviço")
    with st.form(key='marcar_horario_form'):
        data = st.date_input('Data')
        hora = st.time_input('Hora')
        servico = st.selectbox('Serviço', ['1 - Agendar limpeza', '2 - Aplicação de inseticida'])
        submit_button = st.form_submit_button(label='Marcar')
        
        if submit_button:
            servico_code = servico.split(' ')[0]
            agendamento = Horariomarcado(data, hora, servico_code)
            resultado = agendamento.marcarhorario()
            st.success(resultado)
