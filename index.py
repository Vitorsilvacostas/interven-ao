import tkinter as tk
from tkinter import messagebox, ttk

# Lista para armazenar os cursos e informações pessoais
cadastros = []


class GerenciamentoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Cursos do Exército")
        self.root.geometry("400x500")

        self.frame_inicial = tk.Frame(self.root)
        self.frame_inicial.pack(fill="both", expand=True)

        self.frame_incluir = tk.Frame(self.root)
        self.frame_consultar = tk.Frame(self.root)
        self.frame_alterar = tk.Frame(self.root)
        self.frame_excluir = tk.Frame(self.root)

        # Criando os elementos de cada tela apenas uma vez
        self.criar_tela_inicial()
        self.criar_tela_incluir()
        self.criar_tela_consultar()
        self.criar_tela_alterar()
        self.criar_tela_excluir()

        # Bind para validar números
        self.entrada_cpf.bind("<KeyRelease>", self.validar_numeros)
        self.entrada_numero.bind("<KeyRelease>", self.validar_numeros)
        self.entrada_nascimento.bind("<KeyRelease>", self.validar_numeros)

        # Para controlar a mensagem de erro
        self.mensagem_erro_numeros_exibida = False

    def criar_tela_inicial(self):
        tk.Label(self.frame_inicial, text="Selecione uma opção:").pack(pady=10)

        btn_incluir = tk.Button(self.frame_inicial, text="Incluir Cadastro", command=self.abrir_tela_incluir)
        btn_incluir.pack(pady=5, ipadx=20, ipady=10, anchor="center")

        btn_consultar = tk.Button(self.frame_inicial, text="Consultar Cadastros", command=self.abrir_tela_consultar)
        btn_consultar.pack(pady=5, ipadx=20, ipady=10, anchor="center")

        btn_alterar = tk.Button(self.frame_inicial, text="Alterar Cadastro", command=self.abrir_tela_alterar)
        btn_alterar.pack(pady=5, ipadx=20, ipady=10, anchor="center")

        btn_excluir = tk.Button(self.frame_inicial, text="Excluir Cadastro", command=self.abrir_tela_excluir)
        btn_excluir.pack(pady=5, ipadx=20, ipady=10, anchor="center")

    def criar_tela_incluir(self):
        tk.Label(self.frame_incluir, text="Selecione o curso:").pack(pady=5)
        cursos = ["Infantaria", "Cavalaria", "Artilharia", "Comunicações", "Material Bélico", "Engenharia"]
        self.curso_selecionado = tk.StringVar(self.frame_incluir)
        self.curso_selecionado.set(cursos[0])  # valor padrão
        tk.OptionMenu(self.frame_incluir, self.curso_selecionado, *cursos).pack(pady=5)

        tk.Label(self.frame_incluir, text="Nome Completo:").pack(pady=5)
        self.entrada_nome = tk.Entry(self.frame_incluir)
        self.entrada_nome.pack(pady=5)

        tk.Label(self.frame_incluir, text="CPF:").pack(pady=5)
        self.entrada_cpf = tk.Entry(self.frame_incluir)
        self.entrada_cpf.pack(pady=5)

        tk.Label(self.frame_incluir, text="E-mail:").pack(pady=5)
        self.entrada_email = tk.Entry(self.frame_incluir)
        self.entrada_email.pack(pady=5)

        tk.Label(self.frame_incluir, text="Número de Telefone:").pack(pady=5)
        self.entrada_numero = tk.Entry(self.frame_incluir)
        self.entrada_numero.pack(pady=5)

        tk.Label(self.frame_incluir, text="Ano de Nascimento:").pack(pady=5)
        self.entrada_nascimento = tk.Entry(self.frame_incluir)
        self.entrada_nascimento.pack(pady=5)

        tk.Button(self.frame_incluir, text="Salvar", command=self.salvar_cadastro).pack(pady=5, ipadx=20, ipady=10,
                                                                                        anchor="center")
        tk.Button(self.frame_incluir, text="Voltar", command=self.voltar_para_inicial).pack(pady=5, ipadx=20, ipady=10,
                                                                                            anchor="center")

    def criar_tela_consultar(self):
        tk.Label(self.frame_consultar, text="Consultas de Cadastros:").pack(pady=10)

        self.tabela_consulta = ttk.Treeview(self.frame_consultar,
                                            columns=("Curso", "Nome", "CPF", "E-mail", "Telefone", "Nascimento"),
                                            show="headings")
        self.tabela_consulta.heading("Curso", text="Curso")
        self.tabela_consulta.heading("Nome", text="Nome")
        self.tabela_consulta.heading("CPF", text="CPF")
        self.tabela_consulta.heading("E-mail", text="E-mail")
        self.tabela_consulta.heading("Telefone", text="Telefone")
        self.tabela_consulta.heading("Nascimento", text="Nascimento")
        self.tabela_consulta.pack(pady=10)

        tk.Button(self.frame_consultar, text="Voltar", command=self.voltar_para_inicial).pack(pady=20, ipadx=20,
                                                                                              ipady=10, anchor="center")

    def criar_tela_alterar(self):
        tk.Label(self.frame_alterar, text="Selecionar Cadastro para Alteração:").pack(pady=10)

        self.tabela_alterar = ttk.Treeview(self.frame_alterar,
                                           columns=("Curso", "Nome", "CPF", "E-mail", "Telefone", "Nascimento"),
                                           show="headings")
        self.tabela_alterar.heading("Curso", text="Curso")
        self.tabela_alterar.heading("Nome", text="Nome")
        self.tabela_alterar.heading("CPF", text="CPF")
        self.tabela_alterar.heading("E-mail", text="E-mail")
        self.tabela_alterar.heading("Telefone", text="Telefone")
        self.tabela_alterar.heading("Nascimento", text="Nascimento")
        self.tabela_alterar.pack(pady=10)

        tk.Button(self.frame_alterar, text="Alterar", command=self.alterar_cadastro).pack(pady=5, ipadx=20, ipady=10,
                                                                                          anchor="center")
        tk.Button(self.frame_alterar, text="Voltar", command=self.voltar_para_inicial).pack(pady=5, ipadx=20, ipady=10,
                                                                                            anchor="center")

    def criar_tela_excluir(self):
        tk.Label(self.frame_excluir, text="Excluir Cadastro:").pack(pady=10)

        self.tabela_excluir = ttk.Treeview(self.frame_excluir,
                                           columns=("Curso", "Nome", "CPF", "E-mail", "Telefone", "Nascimento"),
                                           show="headings")
        self.tabela_excluir.heading("Curso", text="Curso")
        self.tabela_excluir.heading("Nome", text="Nome")
        self.tabela_excluir.heading("CPF", text="CPF")
        self.tabela_excluir.heading("E-mail", text="E-mail")
        self.tabela_excluir.heading("Telefone", text="Telefone")
        self.tabela_excluir.heading("Nascimento", text="Nascimento")
        self.tabela_excluir.pack(pady=10)

        tk.Button(self.frame_excluir, text="Excluir", command=self.excluir_cadastro).pack(pady=5, ipadx=20, ipady=10,
                                                                                          anchor="center")
        tk.Button(self.frame_excluir, text="Voltar", command=self.voltar_para_inicial).pack(pady=5, ipadx=20, ipady=10,
                                                                                            anchor="center")

    def abrir_tela_incluir(self):
        self.mostrar_frame(self.frame_incluir)

    def abrir_tela_consultar(self):
        self.mostrar_frame(self.frame_consultar)

        # Limpa a tabela antes de popular
        self.tabela_consulta.delete(*self.tabela_consulta.get_children())

        if cadastros:
            for cadastro in cadastros:
                self.tabela_consulta.insert("", tk.END, values=(cadastro["curso"], cadastro["nome"],
                                                                cadastro["cpf"], cadastro["email"],
                                                                cadastro["numero"], cadastro["nascimento"]))

    def abrir_tela_alterar(self):
        self.mostrar_frame(self.frame_alterar)

        # Limpa a tabela antes de popular
        self.tabela_alterar.delete(*self.tabela_alterar.get_children())

        if cadastros:
            for cadastro in cadastros:
                self.tabela_alterar.insert("", tk.END, values=(cadastro["curso"], cadastro["nome"],
                                                               cadastro["cpf"], cadastro["email"],
                                                               cadastro["numero"], cadastro["nascimento"]))

    def abrir_tela_excluir(self):
        self.mostrar_frame(self.frame_excluir)

        self.tabela_excluir.delete(*self.tabela_excluir.get_children())

        if cadastros:
            for cadastro in cadastros:
                self.tabela_excluir.insert("", tk.END, values=(cadastro["curso"], cadastro["nome"],
                                                               cadastro["cpf"], cadastro["email"],
                                                               cadastro["numero"], cadastro["nascimento"]))

    def voltar_para_inicial(self):
        self.mostrar_frame(self.frame_inicial)

    def mostrar_frame(self, frame):
        self.frame_inicial.pack_forget()
        self.frame_incluir.pack_forget()
        self.frame_consultar.pack_forget()
        self.frame_alterar.pack_forget()
        self.frame_excluir.pack_forget()
        frame.pack(fill="both", expand=True)

    def salvar_cadastro(self):
        curso = self.curso_selecionado.get()
        nome = self.entrada_nome.get()
        cpf = self.entrada_cpf.get()
        email = self.entrada_email.get()
        numero = self.entrada_numero.get()
        nascimento = self.entrada_nascimento.get()

        if not (nome and cpf and email and numero and nascimento):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        novo_cadastro = {"curso": curso, "nome": nome, "cpf": cpf, "email": email, "numero": numero,
                         "nascimento": nascimento}
        cadastros.append(novo_cadastro)
        self.limpar_campos()
        messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso.")

    def alterar_cadastro(self):
        item_selecionado = self.tabela_alterar.selection()
        if item_selecionado:
            indice = self.tabela_alterar.index(item_selecionado[0])
            cadastro = cadastros[indice]

            # Criar uma nova janela para edição
            self.janela_edicao = tk.Toplevel(self.root)
            self.janela_edicao.title("Alterar Cadastro")
            self.janela_edicao.geometry("300x300")

            tk.Label(self.janela_edicao, text="Nome Completo:").pack(pady=5)
            self.entrada_nome_alterar = tk.Entry(self.janela_edicao)
            self.entrada_nome_alterar.pack(pady=5)
            self.entrada_nome_alterar.insert(tk.END, cadastro["nome"])

            tk.Label(self.janela_edicao, text="CPF:").pack(pady=5)
            self.entrada_cpf_alterar = tk.Entry(self.janela_edicao)
            self.entrada_cpf_alterar.pack(pady=5)
            self.entrada_cpf_alterar.insert(tk.END, cadastro["cpf"])

            tk.Label(self.janela_edicao, text="E-mail:").pack(pady=5)
            self.entrada_email_alterar = tk.Entry(self.janela_edicao)
            self.entrada_email_alterar.pack(pady=5)
            self.entrada_email_alterar.insert(tk.END, cadastro["email"])

            tk.Label(self.janela_edicao, text="Número de Telefone:").pack(pady=5)
            self.entrada_numero_alterar = tk.Entry(self.janela_edicao)
            self.entrada_numero_alterar.pack(pady=5)
            self.entrada_numero_alterar.insert(tk.END, cadastro["numero"])

            tk.Label(self.janela_edicao, text="Ano de Nascimento:").pack(pady=5)
            self.entrada_nascimento_alterar = tk.Entry(self.janela_edicao)
            self.entrada_nascimento_alterar.pack(pady=5)
            self.entrada_nascimento_alterar.insert(tk.END, cadastro["nascimento"])

            tk.Button(self.janela_edicao, text="Salvar Alterações",
                      command=lambda: self.salvar_alteracoes(indice)).pack(pady=10)

    def salvar_alteracoes(self, indice):
        nome = self.entrada_nome_alterar.get()
        cpf = self.entrada_cpf_alterar.get()
        email = self.entrada_email_alterar.get()
        numero = self.entrada_numero_alterar.get()
        nascimento = self.entrada_nascimento_alterar.get()

        if not (nome and cpf and email and numero and nascimento):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        cadastros[indice] = {"curso": cadastros[indice]["curso"], "nome": nome, "cpf": cpf, "email": email,
                             "numero": numero, "nascimento": nascimento}
        messagebox.showinfo("Sucesso", "Cadastro alterado com sucesso.")
        self.janela_edicao.destroy()  # Fecha a janela de edição
        self.abrir_tela_alterar()  # Atualiza a tabela

    def excluir_cadastro(self):
        item_selecionado = self.tabela_excluir.selection()
        if item_selecionado:
            indice = self.tabela_excluir.index(item_selecionado[0])
            del cadastros[indice]
            messagebox.showinfo("Sucesso", "Cadastro excluído com sucesso.")
            self.abrir_tela_excluir()

    def limpar_campos(self):
        self.curso_selecionado.set("Infantaria")
        self.entrada_nome.delete(0, tk.END)
        self.entrada_cpf.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        self.entrada_numero.delete(0, tk.END)
        self.entrada_nascimento.delete(0, tk.END)

    def validar_numeros(self, event):
        campo = event.widget
        valor = campo.get()

        if not valor.isdigit():
            if not self.mensagem_erro_numeros_exibida:
                messagebox.showerror("Erro", "Este campo só aceita números.")
                self.mensagem_erro_numeros_exibida = True
            campo.delete(len(valor) - 1, tk.END)
        else:
            self.mensagem_erro_numeros_exibida = False


if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciamentoApp(root)
    root.mainloop()

