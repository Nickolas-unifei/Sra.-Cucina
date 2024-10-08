from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Estilo CSS direto no Python
style = """
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    header {
        background-color: #333;
        color: #fff;
        padding: 15px;
        text-align: center;
    }
    nav a {
        color: #fff;
        text-decoration: none;
        margin: 0 10px;
    }
    main {
        padding: 20px;
    }
    h1, h2 {
        color: #333;
    }
    .logo {
        width: 150px;
        height: auto;
        margin-top: 10px;
    }
</style>
"""

# Função para gerar o layout básico da página
def render_page(content):
    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gastronomia para Eventos</title>
        {style}
    </head>
    <body>
        <header>
            <h1>Bem-vindo à Nossa Gastronomia</h1>
            <img src="/static/logo.png" alt="Logo da Empresa" class="logo">  <!-- Logo da empresa -->
            <nav>
                <a href="/">Home</a>
                <a href="/about">Sobre Nós</a>
                <a href="/services">Serviços</a>
                <a href="/contact">Contato</a>
            </nav>
        </header>
        <main>
            {content}
        </main>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = """
        <h2>Experiência Gastronômica para Eventos Inesquecíveis</h2>
        <p>Oferecemos serviços completos de gastronomia para eventos, jantares e muito mais.</p>
        <p><a href="/download/cardapio">Baixe nosso cardápio</a></p> <!-- Link para download do cardápio -->
    """
    return render_page(content)

@app.route('/about')
def about():
    content = """
        <h2>Excelência em Gastronomia para Eventos</h2>
        <p>Somos uma equipe de chefs e profissionais dedicados à criação de experiências gastronômicas únicas.</p>
    """
    return render_page(content)

@app.route('/services')
def services():
    content = """
        <h2>Serviços que Oferecemos</h2>
        <ul>
            <li>Buffet completo para eventos</li>
            <li>Jantares personalizados</li>
            <li>Open Houses e celebrações</li>
            <li>Consultoria em gastronomia</li>
        </ul>
    """
    return render_page(content)

@app.route('/contact')
def contact():
    content = """
        <h2>Entre em Contato</h2>
        <p>Email: contato@empresa.com</p>
        <p>Telefone: (11) 1234-5678</p>
        <p>Endereço: Rua Exemplo, 123, São Paulo, SP</p>
    """
    return render_page(content)

# Rota para o download do cardápio
@app.route('/download/cardapio')
def download_cardapio():
    return send_from_directory('static', 'cardapio.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
