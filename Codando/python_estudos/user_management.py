from verificar_cpf import VerificadorCPF


class UserManagement:
    def __init__(self):
        self.user_dados = []

    def add_user(self, cpf, nome, celular, email, cep, rua, bairro, numero):
        cpf = input('Por favor, insira seu cpf: \n')
        
        validador = VerificadorCPF(cpf)
        if validador.verificar_cpf():
            if not any(user['cpf'] == cpf for user in self.user_dados):
                user = {
                    'cpf': cpf,
                    'nome': nome,
                    'celular': celular,
                    'email': email,
                    'cep': cep,
                    'rua': rua,
                    'bairro': bairro,
                    'numero': numero
                }
                self.user_dados.append(user)
                return 'Usuário adicionado com sucesso!'
            else:
                return 'CPF já cadastrado!'
        else:
            return 'CPF inválido!'

    def atualizar_user(self, cpf, nome=None, celular=None, email=None, cep=None, rua=None, bairro=None, numero=None):
        for user in self.user_dados:
            if user['cpf'] == cpf:
                    if user['cpf'] == cpf:
                        if nome:
                            user['nome'] = nome
                    if celular:
                        user['celular'] = celular
                    if email:
                        user['email'] = email
                    if cep:
                        user['cep'] = cep
                        user['rua'] = rua
                        user['bairro'] = bairro
                        user['numero'] = numero
                    return "Dados de usuário atualizados"
            return "Usuário não encontrado"
    
    def usuario_por_cpf(self, cpf):
        for user in self.user_dados:
            if user['cpf'] == cpf:
                return user
        return None
    
    def listar_usuarios(self):
        return self.user_dados

