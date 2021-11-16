def parse_parameters(query: str) -> dict:
    """
    Функция предназначена для парсинга параметров из URL
    :param query: исходный URL
    :return: словарь параметров
    """
    params_dict = {}
    parameters_string = query.split('?')
    if len(parameters_string) > 1 and len(parameters_string[1]) > 0:
        parameters_list = parameters_string[1].split('&')
        for param in parameters_list:
            item = param.split('=')
            params_dict[item[0]] = item[1]
        return params_dict
    else:
        return {}


def parse_cookies(query: str) -> dict:
    """
    Функция предназначена для парсинга и преобразования текстовых cookie в словарь
    :param query: текстовый cookie
    :return: словарь ключ:значение всех параметров из cookie
    """
    res_dict = {}
    if len(query) > 0:
        cookie_list = query.split(';')
        for it in cookie_list:
            if len(it) > 0:
                lst_items = it.split('=', 1)
                res_dict[lst_items[0]] = lst_items[1]
        return res_dict
    else:
        return {}


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}

    assert parse_parameters('http://example.com/') == {}

    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret',
                                                                                             'color': 'purple'}

    assert parse_parameters('https://www.coachoutlet.com/shop/clearance/view-all?') == {}
    assert parse_parameters('https://www.coachoutlet.com/shop/clearance/view-all?utm_source=SUMO3&'
                            'utm_campaign=50220e8db6-EMAIL_CAMPAIGN_2019_03_11_11_49_COPY_01&utm_medium=email&'
                            'utm_term=0_fca091d938-50220e8db6-134247207') == \
           {'utm_source': 'SUMO3',
            'utm_campaign': '50220e8db6-EMAIL_CAMPAIGN_2019_03_11_11_49_COPY_01',
            'utm_medium': 'email',
            'utm_term': '0_fca091d938-50220e8db6-134247207'}

    assert parse_parameters('https://stepik.org/course/72969/promo?after_pass_reset=true') == \
           {'after_pass_reset': 'true'}

    assert parse_parameters('https://www.youtube.com/watch?v=nWjrZtskIWs&list=PLQAt0m1f9OHtfXxDph-MJvYCLaOvildGQ') == \
           {'v': 'nWjrZtskIWs', 'list': 'PLQAt0m1f9OHtfXxDph-MJvYCLaOvildGQ'}

    assert parse_parameters('https://parts66.ru/manuals/?mbrid=4&trid=6281') == {'mbrid': '4', 'trid': '6281'}

    assert parse_parameters('http://forum.e30club.com.ua/index.php?topic=1097.0') == {'topic': '1097.0'}

    # Tests for function "parse_cookies"
    # assert parse_cookies('') == {}
    # assert parse_cookies('name=Dima;') == {'name': 'Dima'}

    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('name=Dima') == {'name': 'Dima'}

    # rozetka.ua
    assert parse_cookies('ab-cart-se=new;slang=ru;uid=rB4eC2GOx8hhl9lF1T4HAg==;xab_segment=136;'
                         'xl_uid=ThvGqWGOx8cx0j3cB9HiAg==') == {'ab-cart-se': 'new', 'slang': 'ru',
                                                                'uid': 'rB4eC2GOx8hhl9lF1T4HAg==', 'xab_segment': '136',
                                                                'xl_uid': 'ThvGqWGOx8cx0j3cB9HiAg=='}
    # gmail.com
    assert parse_cookies('__Host-GAPS=1:aFM-6ZhQKqUoPpUMXKJ06i-iOPim-w:FRzmluYd5mu4E3aP') == \
           {'__Host-GAPS': '1:aFM-6ZhQKqUoPpUMXKJ06i-iOPim-w:FRzmluYd5mu4E3aP'}
    # linkedin.com
    assert parse_cookies('bcookie="v=2&075bf757-83f3-4d02-8e79-429dd27dcca8";lang=v=2&lang=en-us;'
                         'lidc="b=TGST00:s=T:r=T:a=T:p=T:g=2734:u=1:x=1:i=1636751001:t=1636837401:v=2:'
                         'sig=AQERdB10prMuB2RjRiRf3MAX_rUWpyMP";JSESSIONID=ajax:0901270690555964416;'
                         'bscookie="v=1&20211112210321c5a36b5e-1f2d-468e-87eb-da801c92f5e3AQGEad3jnIg0Tmmo4QrCQy-cEN'
                         '--G6CD"') == \
           {'bcookie': '"v=2&075bf757-83f3-4d02-8e79-429dd27dcca8"',
            'lang': 'v=2&lang=en-us',
            'lidc': '"b=TGST00:s=T:r=T:a=T:p=T:g=2734:u=1:x=1:i=1636751001:t=1636837401:v=2:sig'
                    '=AQERdB10prMuB2RjRiRf3MAX_rUWpyMP"',
            'JSESSIONID': 'ajax:0901270690555964416',
            'bscookie': '"v=1&20211112210321c5a36b5e-1f2d-468e-87eb-da801c92f5e3AQGEad3jnIg0Tmmo4QrCQy-cEN--G6CD"'}

    # udemy.com
    assert parse_cookies('__cf_bm=oFSV1dXwKlH9eQdmiiSHpHruFOVoJu1.4Wcg70xk8vw-1636751445-0-AUkjNJxhIi8q11xkzBw7Rl1A/2DJ'
                         'LwdH4yI0IzZR/oirj4ldMA0En/sGsS9Z4N6TRidmruCPQnFwiCLTSISWMJ0=;__cfruid=7a12d67068801df84f00a22'
                         '3b0d195b91aee2f4d-1636751445;__udmy_2_v57r=0d6fc25ec867490ca1eba530268bb617;csrftoken=TeaMcn3'
                         'XecKT0Fhqdn1HEHoa29F9IlyoD6N9LhIzBNud7gPweG0IzdWRqu76AqvE;evi="3@Br4JIUOqQ49xXr6OpXqz1LQYgri1'
                         'q6BkyerW-K6lB9oyWkS3nQeSyQVpXfgPI31xeco1-SBGrAvnXTnNlUyC_HCmBUdC5gGafdnq06wgyTmX20HzuzK3Z6kNq'
                         'Ctdg6iseuI655rA3bztNiY5pSTUyt7edYyJtFQqhHQEEsvoOGVQXpDiC9rj4_wcIUDv8dgg0-Ue3ujtDzMr_GW-9lKuUP'
                         'mpNORCO3A=";seen=1;ud_cache_brand=UAen_US;ud_cache_campaign_code=NEWTOLEARNING;ud_cache_devic'
                         'e=None;ud_cache_language=en;ud_cache_logged_in=0;ud_cache_marketplace_country=UA;ud_cache_mod'
                         'ern_browser=0;ud_cache_price_country=UA;ud_cache_release=daf593b914755c47c8c6;ud_cache_user="'
                         '";ud_cache_version=1;ud_firstvisit=2021-11-12T21:10:45.149330+00:00:1mldor:KmrA1RklgVcizZZqnN'
                         'xYBgIr8rs;ud_rule_vars="eJyFjs0KgzAQhF9Fcu0Pm6jR5lkCYY2rDS0N3UQv4rs30BZ6K8xpmG9mNpGRZ8o0ujWkk'
                         'CMbGPXkVUu-111zAY-SBmxrULofBi0742O8BRKmEpsVU-CU36wbMZMtvhUKlDzJIlUpaSSYpj3LRuq6PwAYACuOJXXHgu'
                         'a4-KvLjNMUvEtxYU9uRQ443D9tkWd8BP8DMT0XSv8Wy9m2676Lu9hfx0ZH6Q==:1mldor:9ZYJQeggGCr4l0xibJLYxH2'
                         'qy2w"') == \
           {'__cf_bm': 'oFSV1dXwKlH9eQdmiiSHpHruFOVoJu1.4Wcg70xk8vw-1636751445-0-AUkjNJxhIi8q11xkzBw7Rl1A'
            '/2DJLwdH4yI0IzZR/oirj4ldMA0En/sGsS9Z4N6TRidmruCPQnFwiCLTSISWMJ0=', '__cfruid': '7a12d67068801df84f00a223b0'
            'd195b91aee2f4d-1636751445', '__udmy_2_v57r': '0d6fc25ec867490ca1eba530268bb617',
            'csrftoken': 'TeaMcn3XecKT0Fhqdn1HEHoa29F9IlyoD6N9LhIzBNud7gPweG0IzdWRqu76AqvE',
            'evi': '"3@Br4JIUOqQ49xXr6OpXqz1LQYgri1q6BkyerW-K6lB9oyWkS3nQeSyQVpXfgPI31xeco1'
                   '-SBGrAvnXTnNlUyC_HCmBUdC5gGafdnq06wgyTmX20HzuzK3Z6kNqCtdg6iseuI655rA3bztNiY5pSTUyt7edYyJtFQqhHQEEsv'
                   'oOGVQXpDiC9rj4_wcIUDv8dgg0-Ue3ujtDzMr_GW-9lKuUPmpNORCO3A="',
            'seen': '1', 'ud_cache_brand': 'UAen_US', 'ud_cache_campaign_code': 'NEWTOLEARNING',
            'ud_cache_device': 'None', 'ud_cache_language': 'en', 'ud_cache_logged_in': '0',
            'ud_cache_marketplace_country': 'UA', 'ud_cache_modern_browser': '0', 'ud_cache_price_country': 'UA',
            'ud_cache_release': 'daf593b914755c47c8c6', 'ud_cache_user': '""', 'ud_cache_version': '1',
            'ud_firstvisit': '2021-11-12T21:10:45.149330+00:00:1mldor:KmrA1RklgVcizZZqnNxYBgIr8rs',
            'ud_rule_vars': '"eJyFjs0KgzAQhF9Fcu0Pm6jR5lkCYY2rDS0N3UQv4rs30BZ6K8xpmG9mNpGRZ8o0ujWkkCMbGPXkVUu-111zAY'
                            '-SBmxrULofBi0742O8BRKmEpsVU-CU36wbMZMtvhUKlDzJIlUpaSSYpj3LRuq6PwAYACuOJXXHgua4'
                            '-KvLjNMUvEtxYU9uRQ443D9tkWd8BP8DMT0XSv8Wy9m2676Lu9hfx0ZH6Q==:1mldor'
                            ':9ZYJQeggGCr4l0xibJLYxH2qy2w"'}

    # ottplayer.tv
    assert parse_cookies('_gid=GA1.2.1144699608.1637063265;lang=959c472886bf6d334bf6dd1ebbab1166bc3ef304%7Een;session=a'
                         '4964567112a448152b2a02a8aa975e631b43b15%7E61939a633f2ed5-32101544;1P_JAR=2021-11-09-18;NID=51'
                         '1=URe588PXZsFC7Fbf4znMq46e6v4MFFD5NgPX1QKANzx1-3S_k1mgCKHOf5d6xI_Hh-N6IezrFAkEKbiMwO34_ukwiLL'
                         'jackn_pOH2CMlIYLLwjxdGDwqH38Z8G3d8OgpCYwFzTrZaQGyxEcgw-RvvdBfIlaP_aIpy2OL1EK1Pes') == \
           {'_gid': 'GA1.2.1144699608.1637063265', 'lang': '959c472886bf6d334bf6dd1ebbab1166bc3ef304%7Een',
            'session': 'a4964567112a448152b2a02a8aa975e631b43b15%7E61939a633f2ed5-32101544', '1P_JAR': '2021-11-09-18',
            'NID': '511=URe588PXZsFC7Fbf4znMq46e6v4MFFD5NgPX1QKANzx1-3S_k1mgCKHOf5d6xI_Hh-N6IezrFAkEKbiMwO34_ukwiLLjac'
            'kn_pOH2CMlIYLLwjxdGDwqH38Z8G3d8OgpCYwFzTrZaQGyxEcgw-RvvdBfIlaP_aIpy2OL1EK1Pes'}
