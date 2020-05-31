import requests
import json
from datetime import datetime

MOCKED = True
VALID_WORDS = ["corona", "covid", "morte", "pandemia", "mascara", "covid19", "covid-19", "hospitais", "pulmão", "pulmões", "coronavírus", "mortes", "distanciamento"]
INVALID_WORDS = ["treino", "treinos", "futebol", "bola", "jogador", "jogadores", "jogos"]

def query_news(city):
    city = city.strip()
    url = (f'https://newsapi.org/v2/everything?domains=terra.com.br,uol.com.br,globo&q={city}&pageSize=12&apiKey=5c3349b9af944d3a8838be33a30ca9e8')

    response = ''
    n_res = {
      "filled": False,
      "author": '',
      "title": '',
      "description": '',
      "url": '',
      "urlToImage": '',
      "publishedAt": '',
    }
    if not MOCKED:
        response = requests.get(url).json()
    else:
        response = _new_mock()

    articles = response["articles"]
    sorted_articles = sorted(articles, key=lambda x: datetime.strptime(x['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'))

    for article in sorted_articles:
        if __valid_new(article):
            n_res["filled"] = True
            n_res["author"] = article["author"]
            n_res["title"] = article["title"]
            n_res["description"] = article["description"]
            n_res["url"] = article["url"]
            n_res["urlToImage"] = article["urlToImage"]
            n_res["publishedAt"] = article["publishedAt"]

    

    return n_res


def __valid_new(new):
    for vw in VALID_WORDS:
        for iw in INVALID_WORDS:
            title = new["title"].lower()
            description = new["description"]
            if vw in title and iw not in title:
                return True
            if vw in description and iw not in description:
                return True
    return False


def _new_mock():
    return {
  "status": "ok",
  "totalResults": 228,
    "articles": [
    {
      "source": { "id": None, "name": "B9.com.br" },
      "author": "Soraia Alves",
      "title": "Pernambucanas doa 100 mil máscaras para instituições hospitalares",
      "description": "Diante do cenário a0de a0escassez de equipamentos de proteção individual para os profissionais da saúde que estão na linha de frente de a0combate à Covid-19 no Brasil, a Pernambucanas realiza a0uma doação de 100 mil máscaras cirúrgicas a0para a0instituições hospitalares a0…",
      "url": "https://www.b9.com.br/126502/pernambucanas-mascaras-para-instituicoes-hospitalares/",
      "urlToImage": "https://assets.b9.com.br/wp-content/uploads/2020/05/mascaras-doio-pernambucanas-440x440.jpg",
      "publishedAt": "2020-05-22T18:27:30Z",
      "content": "Diante do cenário a0de a0escassez de equipamentos de proteção individual para os profissionais da saúde que estão na linha de frente de a0combate à Covid-19 no Brasil, a Pernambucanas realiza a0uma doação de… [+1842 chars]"
    },
    {
      "source": { "id": None, "name": "Terra.com.br" },
      "author": "Estadão Conteúdo",
      "title": "Com visitas suspensas, asilos no interior de SP somam 20 idosos mortos por coronavírus",
      "description": "SOROCABA - Ao menos 20 idosos já morreram em asilos do interior de São Paulo por covid-19. Pelo ...",
      "url": "https://www.terra.com.br/vida-e-estilo/saude/com-visitas-suspensas-asilos-no-interior-de-sp-somam-20-idosos-mortos-por-coronavirus,68eb52f318a28045dd4ecb4f4eb3a8ee0fv55jao.html",
      "urlToImage": "http://p2.trrsf.com/image/fget/cf/800/450/middle/s1.trrsf.com/atm/3/core/_img/terra-logo-white-bg-v3.jpg",
      "publishedAt": "2020-05-07T15:12:13Z",
      "content": "SOROCABA - Ao menos 20 idosos já morreram em asilos do interior de São Paulo por covid-19. Pelo menos dois óbitos suspeitos estão em investigação. Há também pacientes em isolamento ou internados com … [+6495 chars]"
    },
    {
      "source": { "id": None, "name": "Purepeople.com.br" },
      "author": "PurePeople",
      "title": "Biah Rodrigues planeja 2ª gravidez e comenta relação com Maiara. Saiba!",
      "description": "Mulher de Sorocaba, Biah Rodrigues está com 9 meses de gravidez e já tem planos de ter o 2º filho. A modelo destacou, em entrevista para colunista, ansiedade para nascimento do herideiro e relação com Maiara, dupla de Maraisa. 'Ela não é ciumenta (risos). Só …",
      "url": "https://www.purepeople.com.br/noticia/mulher-de-sorocaba-dispara-sobre-gravidez-e-ciumes-de-maiara-dupla-de-maraisa_a293713/1",
      "urlToImage": "http://p2.trrsf.com/image/fget/cf/800/450/middle/images.terra.com/2020/05/15/3323665-mulher-de-sorocaba-biah-rodrigues-revel-650x488-2.jpg",
      "publishedAt": "2020-05-15T13:31:09Z",
      "content": "Mulher se Sorocaba, Biah Rodrigues está na reta final da gravidez do primeiro filho, mas já tem planos de se tornar mãe de novo. A modelo, em entrevista para a coluna da Fábio Oliveira, do O Dia, rev… [+2336 chars]"
    },
    {
      "source": { "id": None, "name": "Purepeople.com.br" },
      "author": "PurePeople",
      "title": "Mulher de Sorocaba, Biah Rodrigues dá 1º banho no filho, Theo:'Estou aprendendo'",
      "description": "Biah Rodrigues apareceu em foto dando o primeiro banho no filho, Theo, fruto do seu casamento com o sertanejo Sorocaba. 'Estou aprendendo ainda. Não me julguem', escreveu bem-humorada a mamãe de primeira viagem. A modelo ganhou apoio dos seguidores. 'Quando n…",
      "url": "https://www.purepeople.com.br/noticia/biah-rodrigues-aparece-em-foto-dando-1-banho-no-filho-nao-me-julguem_a294364/1",
      "urlToImage": "http://p2.trrsf.com/image/fget/cf/800/450/middle/images.terra.com/2020/05/26/3330580-biah-rodrigues-deu-o-1-banho-no-seu-fil-650x488-1.jpg",
      "publishedAt": "2020-05-26T17:07:59Z",
      "content": "Mamãe de primeira viagem, Biah Rodrigues deu o primeiro banho no filho, Theo, nascido no último dia 17. A mulher de Sorocaba, parceiro de palco de Fernando, compartilhou o registro em seu Instagram e… [+2527 chars]"
    },
    {
      "source": { "id": None, "name": "Purepeople.com.br" },
      "author": "PurePeople",
      "title": "Maiara e Fernando ganham torcida de famosos por casamento: 'Ano que vem'",
      "description": "A dupla de Maraisa fez uma participação na live do namorado, Fernando Zor. O cantor, parceiro de Sorocaba nos palcos, foi fotografado com a ruiva em clima de romance e, nas redes sociais, ela não escondeu a vontade de subir ao altar. 'Sigo na esperança de ca…",
      "url": "https://www.purepeople.com.br/noticia/beijo-de-maiara-com-namorado-fernando-tem-detalhe-curioso-apontado-pela-cantora-foto_a293404/1",
      "urlToImage": "http://p2.trrsf.com/image/fget/cf/800/450/middle/images.terra.com/2020/05/10/3320128-famosas-torcem-por-casamento-de-maiara-e-650x488-1.png",
      "publishedAt": "2020-05-10T12:53:21Z",
      "content": "Maiara, dupla de Maraisa, marcou presença na live do namorado, Fernando Zor. O cantor se apresentou em transmissão de vídeo do Youtube com Sorocaba na noite de sábado (10). Após a apresentação, a rui… [+499 chars]"
    },
    {
      "source": { "id": None, "name": "Uol.com.br" },
      "author": "UOL",
      "title": "Com Theo | Sorocaba e Biah Rodrigues deixam a maternidade",
      "description": "O sertanejo Sorocaba, que faz dupla com Fernando Zor, e a mulher, Biah Rodrigues, deixaram hoje a maternidade em São Paulo com o primeiro filho deles, Theo, que nasceu no domingo (17). Biah postou no Instagram uma foto com o bebê no colo, recebendo um bei",
      "url": "https://tvefamosos.uol.com.br/noticias/redacao/2020/05/19/sorocaba-e-biah-rodrigues-deixam-maternidade-com-o-filho-theo.htm",
      "urlToImage": "https://conteudo.imguol.com.br/c/entretenimento/83/2020/05/19/sorocaba-a-mulher-biah-rodrigues-e-o-filho-do-casal-theo-1589929797518_v2_615x300.jpg",
      "publishedAt": "2020-05-19T23:31:16Z",
      "content": "O sertanejo Sorocaba, que faz dupla com Fernando Zor, e a mulher, Biah Rodrigues, deixaram hoje a maternidade em São Paulo com o primeiro filho deles, Theo, que nasceu no domingo (17). Biah postou no… [+896 chars]"
    },
    {
      "source": { "id": None, "name": "Purepeople.com.br" },
      "author": "PurePeople",
      "title": "Isolados em fazenda, Biah Rodrigues decora chá de bebê do filho com Sorocaba",
      "description": "Dupla de Fernando, Sorocaba e a mulher, Biah Rodrigues, realizaram o chá de bebê do primeiro filho, Theo, neste sábado (2). Isolados na propriedade do cantor, a influencer ficou responsável por decorar a festinha, que teve fazenda como tema. Ela contou com a …",
      "url": "https://www.purepeople.com.br/noticia/fotos-dupla-de-fernando-sorocaba-faz-cha-de-bebe-do-filho-com-biah-rodrigues-em-quarentena_a292984/1",
      "urlToImage": "http://p2.trrsf.com/image/fget/cf/800/450/middle/images.terra.com/2020/05/03/3315445-cantor-sorocaba-e-a-mulher-biah-rodrigu-650x488-2.jpg",
      "publishedAt": "2020-05-03T13:38:56Z",
      "content": "Biah Rodrigues e Sorocaba promoveram o chá de bebê do primeiro filho, Theo, neste sábado (2). Isolados na propriedade rural da dupla de Fernando por causa da pandemia do Covid-19, o casal curtiu a co… [+2286 chars]"
    },
    {
      "source": { "id": None, "name": "Terra.com.br" },
      "author": "Estadão Conteúdo",
      "title": "Com 25 mortes por coronavírus, sistema prisional continuará sem visita em SP",
      "description": "Segundo a Secretaria de Administração Penitenciária, 12 óbitos são de detentos e 13 de funcionários",
      "url": "https://www.terra.com.br/vida-e-estilo/saude/com-25-mortes-por-coronavirus-sistema-prisional-continuara-sem-visita-em-sp,75337fb53658d9b9dadd8cb8c3604c28diu4ea5f.html",
      "urlToImage": "http://p2.trrsf.com/image/fget/cf/800/450/middle/s1.trrsf.com/atm/3/core/_img/terra-logo-white-bg-v3.jpg",
      "publishedAt": "2020-05-29T23:58:13Z",
      "content": "SOROCABA - Apesar das medidas de flexibilização das atividades econômicas anunciadas pelo governo paulista, os presos do sistema prisional de São Paulo continuarão sem receber visitas de familiares. … [+1319 chars]"
    },
    {
      "source": { "id": None, "name": "Purepeople.com.br" },
      "author": "PurePeople",
      "title": "Giselle Itié se diverte ao ser 'atacada' pelo filho: 'Bebê babão'. Veja vídeo!",
      "description": "Giselle Itié é mãe coruja mesmo. A atriz compartilhou em seu Stories um momento de diversão com o filho, Pedro Luna, de 2 meses. Nas imagens, o menino aparece 'atacando' a mãe, levando-a às gargalhadas. 'Bebê babão', brincou a mexicana, que revelou semanas pa…",
      "url": "https://www.purepeople.com.br/noticia/filho-de-giselle-itie-diverte-a-mae-ao-ataca-la-em-video-bebe-babao_a293932/1",
      "urlToImage": "http://p2.trrsf.com/image/fget/cf/800/450/middle/images.terra.com/2020/05/19/3325852-filho-de-giselle-itie-e-guilherme-winter-650x488-1.jpg",
      "publishedAt": "2020-05-19T12:49:28Z",
      "content": "Giselle Itié vem curtindo cada momento ao lado do filho, Pedro Luna, de quase 3 meses. O menino é fruto do seu relacionamento com Guilherme Winter. A atriz dividiu com os seguidores em sua conta de I… [+2435 chars]"
    },
    {
      "source": { "id": None, "name": "Uol.com.br" },
      "author": "UOL",
      "title": "Primeiro filho | Nasce o bebê do sertanejo Sorocaba e de Biah Rodrigues",
      "description": "Nasceu hoje o primeiro filho do sertanejo Sorocaba com sua mulher Biah Rodrigues. Theo chegou ao mundo pontualmente às 18h, na maternidade do Hospital São Luiz, em São Paulo.O bebê, que nasceu de parto normal, foi registrado com 47 centímetros e 2,800 qui",
      "url": "https://tvefamosos.uol.com.br/noticias/redacao/2020/05/17/nasce-o-primeiro-filho-do-sertanejo-sorocaba-e-biah-rodrigues.htm",
      "urlToImage": "https://conteudo.imguol.com.br/c/entretenimento/bb/2020/05/17/biah-rodrigues-e-sorocaba-com-o-recem-nascido-filho-theo-1589760342489_v2_615x300.jpg",
      "publishedAt": "2020-05-18T00:26:21Z",
      "content": "Nasceu hoje o primeiro filho do sertanejo Sorocaba com sua mulher Biah Rodrigues. Theo chegou ao mundo pontualmente às 18h, na maternidade do Hospital São Luiz, em São Paulo.\r\nO bebê, que nasceu de p… [+666 chars]"
    },
    {
      "source": { "id": None, "name": "Uol.com.br" },
      "author": "UOL",
      "title": "Caso em São Paulo | Mecânico morre dois dias após filho ter alta: 'Estava esperando', diz familiar da vítima",
      "description": "Uma família de Sorocaba (SP) conheceu os dois lados da pandemia do coronavírus em menos de 48 horas. Foi esse o tempo entre a alta de Rogério Gonçalves da Silva, 36, e a morte do pai, Narcizo Gonçalves da Silva, 69. Os dois estavam internados na Santa Cas",
      "url": "https://noticias.uol.com.br/cotidiano/ultimas-noticias/2020/05/11/mecanico-morre-de-coronavirus-2-dias-apos-filho-ter-alta-estava-esperando.htm",
      "urlToImage": "https://conteudo.imguol.com.br/c/noticias/8c/2020/05/11/narcizo-goncalves-da-silva-morre-por-coronavirus-1589209527707_v2_615x300.jpg",
      "publishedAt": "2020-05-11T19:27:03Z",
      "content": "Uma família de Sorocaba (SP) conheceu os dois lados da pandemia do coronavírus em menos de 48 horas. Foi esse o tempo entre a alta de Rogério Gonçalves da Silva, 36, e a morte do pai, Narcizo Gonçalv… [+3740 chars]"
    },
    {
      "source": { "id": None, "name": "Conjur.com.br" },
      "author": None,
      "title": "Indeferidos HCs para colocar presos idosos de SP em domiciliar",
      "description": "Três habeas corpus coletivos impetrados pela Defensoria Pública de São Paulo, com o objetivo de colocar em liberdade ou em regime domiciliar presos idosos custodiados nas cidades paulistas de Iperó, Sorocaba e Capela do Alto, foram indeferidos pelos relatores…",
      "url": "https://www.conjur.com.br/2020-mai-07/indeferidos-hcs-colocar-presos-idosos-sp-domiciliar",
      "urlToImage": "https://s.conjur.com.br/img/b/superlotacao-prisao-prisoes-sistema.jpeg",
      "publishedAt": "2020-05-07T13:51:00Z",
      "content": "Três habeas corpus coletivos impetrados pela Defensoria Pública de São Paulo, com o objetivo de colocar em liberdade ou em regime domiciliar presos idosos custodiados nas cidades paulistas de Iperó, … [+4623 chars]"
    },
    {
      "source": { "id": None, "name": "Uol.com.br" },
      "author": "UOL",
      "title": "'Transformador' | Mulher de Sorocaba, Biah Rodrigues fala sobre parto de Theo",
      "description": "Biah Rodrigues, mulher do sertanejo Sorocaba, deu à luz o pequeno Theo no último domingo (17), por meio de parto normal humanizado. Ela ficou tão positivamente impressionada com a experiência que a recomendou a futuras mamães.Em entrevista à \"Quem\", conto",
      "url": "https://tvefamosos.uol.com.br/noticias/redacao/2020/05/20/mulher-de-sorocaba-biah-rodrigues-fala-sobre-parto-transformador.htm",
      "urlToImage": "https://conteudo.imguol.com.br/c/entretenimento/bb/2020/05/17/biah-rodrigues-e-sorocaba-com-o-recem-nascido-filho-theo-1589760342489_v2_615x300.jpg",
      "publishedAt": "2020-05-21T00:01:24Z",
      "content": "Biah Rodrigues, mulher do sertanejo Sorocaba, deu à luz o pequeno Theo no último domingo (17), por meio de parto normal humanizado. Ela ficou tão positivamente impressionada com a experiência que a r… [+934 chars]"
    },
    {
      "source": { "id": None, "name": "Noticiasautomotivas.com.br" },
      "author": "Ricardo de Oliveira",
      "title": "Toyota Yaris com visual mais agressivo é registrado na Argentina",
      "description": "Ele é o XP150 dentro do portfólio de projetos em produção dentro da Toyota. Não é exatamente um carro novo, já que seu lançamento se deu em 2013, com produção iniciada em abril daquele ano. Esse é o Yaris que temos rodando aqui. Contudo, o produto feito em So…",
      "url": "https://www.noticiasautomotivas.com.br/toyota-yaris-com-visual-mais-agressivo-e-registrado-na-argentina/",
      "urlToImage": "https://images.noticiasautomotivas.com.br/img/f/yaris-atualizado.jpg",
      "publishedAt": "2020-05-18T18:04:54Z",
      "content": "Ele é o XP150 dentro do portfólio de projetos em produção dentro da Toyota. Não é exatamente um carro novo, já que seu lançamento se deu em 2013, com produção iniciada em abril daquele ano. Esse é o … [+1703 chars]"
    },
    {
      "source": { "id": None, "name": "Catracalivre.com.br" },
      "author": None,
      "title": "Estudantes de Etec em SP dão curso gratuito de programação pela internet",
      "description": "Três alunos do curso técnico de Informática criaram ambiente virtual que conta com mais de 60 videoaulas gratuitas para iniciantes.",
      "url": "https://catracalivre.com.br/educacao/estudantes-de-etec-em-sp-dao-curso-gratuito-de-programacao-pela-internet/",
      "urlToImage": "https://catracalivre.com.br/wp-content/uploads/2020/05/estudantes-curso-programacao.jpg",
      "publishedAt": "2020-05-18T19:18:40Z",
      "content": "Uma das dicas para lidar com o isolamento social, medida necessária para enfrentar a propagação do novo coronavírus, é investir em cursos online. Pensando em ajudar pessoas que queiram aproveitar o p… [+1896 chars]"
    },
    {
      "source": { "id": None, "name": "Uol.com.br" },
      "author": "UOL",
      "title": "'Nos damos bem' | Em quarentena com Maiara, Fernando Zor avalia casamento",
      "description": "Em tempos de quarentena, muitos casais se aproximaram mais e decidiram viver uma quase vida de casados. Esse é o caso dos cantores Fernando Zor e Maiara, que já vivem um romance de um ano e ficaram mais unidos por vivenciarem juntos a experiência da quare",
      "url": "https://tvefamosos.uol.com.br/noticias/redacao/2020/05/09/fernando-zor-diz-que-quarentena-ao-lado-de-maiara-ja-e-um-casamento.htm",
      "urlToImage": "https://conteudo.imguol.com.br/c/entretenimento/26/2020/05/05/maiara-e-fernando-zor-comemoram-1-ano-juntos-1588700849344_v2_615x300.jpg",
      "publishedAt": "2020-05-09T16:45:44Z",
      "content": "Em tempos de quarentena, muitos casais se aproximaram mais e decidiram viver uma quase vida de casados. Esse é o caso dos cantores Fernando Zor e Maiara, que já vivem um romance de um ano e ficaram m… [+724 chars]"
    },
    {
      "source": { "id": None, "name": "Conjur.com.br" },
      "author": "Tábata Viapiana",
      "title": "Estado deve garantir cuidados aos filhos dos profissionais da saúde",
      "description": "Se o poder público garante a prestação de um serviço público essencial de saúde, pelas mesmas razões deve garantir o suporte necessário para a0sua realização. No caso, deve garantir os cuidados necessários aos filhos dos profissionais de saúde, que não tenham c…",
      "url": "https://www.conjur.com.br/2020-mai-25/estado-garantir-cuidados-aos-filhos-profissionais-saude",
      "urlToImage": "https://s.conjur.com.br/img/b/creche-auxilio-criancas-educadora.jpeg",
      "publishedAt": "2020-05-25T14:11:00Z",
      "content": "Se o poder público garante a prestação de um serviço público essencial de saúde, pelas mesmas razões deve garantir o suporte necessário para a0sua realização. No caso, deve garantir os cuidados necessá… [+2577 chars]"
    },
    {
      "source": { "id": None, "name": "Uol.com.br" },
      "author": "UOL",
      "title": "Feito em Sorocaba | Toyota registra Yaris reestilizado de modelo europeu na Argentina",
      "description": "A Toyota registrou desenhos de um Yaris reestilizado e do modelo europeu na Argentina.Os esboços foram cadastrados no Instituto Nacional da Propriedade Industrial do país, como revelou a revista \"Parabrisas\".A fabricante deve realizar mudanças na dianteir",
      "url": "https://www.uol.com.br/carros/noticias/redacao/2020/05/18/toyota-registra-yaris-reestilizado-e-modelo-europeu-na-argentina.htm",
      "urlToImage": "https://conteudo.imguol.com.br/c/entretenimento/26/2020/05/17/novo-toyota-yaris-1-1589752014256_v2_750x421.jpg",
      "publishedAt": "2020-05-18T12:28:39Z",
      "content": "A Toyota registrou desenhos de um Yaris reestilizado e do modelo europeu na Argentina.\r\nOs esboços foram cadastrados no Instituto Nacional da Propriedade Industrial do país, como revelou a revista \"P… [+1910 chars]"
    },
    {
      "source": { "id": None, "name": "Abril.com.br" },
      "author": "Da Redação",
      "title": "Doria autoriza reabertura com restrições de shoppings da cidade de SP",
      "description": "Não há informações específicas sobre quais os pré-requisitos e quando será a retomada; esses detalhes devem ser estabelecidos pelo prefeito Bruno Covas",
      "url": "https://veja.abril.com.br/saude/doria-autoriza-reabertura-com-restricoes-de-shoppings-da-cidade-de-sp/",
      "urlToImage": "https://abrilveja.files.wordpress.com/2020/04/shopping_iguatemi___1.jpg.jpg?quality=70&strip=info&w=680&h=453&crop=1",
      "publishedAt": "2020-05-27T17:28:44Z",
      "content": "O governador do estado de São Paulo, João Doria, autorizou a reabertura “com restrições” de shoppings da a0cidade de São Paulo e de outras dez regiões paulistas. A medida entra no pacote de flexibiliza… [+1532 chars]"
    },
    {
      "source": { "id": None, "name": "Catracalivre.com.br" },
      "author": None,
      "title": "Números mostram interiorização acelerada do novo coronavírus em SP",
      "description": "Dados da Secretaria Estadual de Saúde mostram que, entre 30 de abril e 18 de maio, o percentual de casos confirmados e mortes por covid-19, em todas as 15 regiões administrativas do estado, superou o índice registrado na Grande SP.",
      "url": "https://catracalivre.com.br/?p=2090293",
      "urlToImage": "https://catracalivre.com.br/wp-content/uploads/2020/05/vista-jundiai-8-1.jpg",
      "publishedAt": "2020-05-27T21:25:05Z",
      "content": "Na última quinta-feira, 21, o ministro da Saúde interino, Eduardo Pazuello, em coletiva à imprensa, admitiu que a interiorização do contágio do novo coronavírus no Brasil é uma questão inevitável.\r\nO… [+5619 chars]"
    }
  ]
}
