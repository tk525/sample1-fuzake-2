import os
from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)
app = Flask(__name__, static_folder='./templates/static') 



@app.route('/')
def hello():
    css = "static/style.css"
    reset_css = "static/reset.css"
    js = "static/main.js"

    # 導入
    post_img = "static/img/self-intro.gif"
    post0 = "LAZIER"
    post1 = "私は面倒くさがりです"

    # 自己紹介
    aboutMe0 = "少し私の経歴の話をしましょう。あれは今から28年前、震災が起こる約7ヶ月前に、関西を初期セーブポイントとして、ステータスは末っ子、滝口結という名前を付与されて誕生しました。"
    aboutMe1="小中学校はPCのオンラインゲームへの情熱を注ぎ、高校在籍時はHTMLとCSSの独学に覚醒しました。"
    aboutMe2="高校卒業後は、複数の異業種及び異職種で経験値獲得とジョブチェンジを行い、2019年よりプログラミング(PHP)と英語を学習するために海外に出征しました。"
    aboutMe3="その期間中、四六時中コードを考えている癖や、「自身の知識を増やししつつ、未知のエラーや実装経験がない機能で更に何かを作りたい」と強い思いから、最終ジョブチェンジを決意しました。"
    aboutMe4="帰還後、独学でPythonの自然言語処理と英語、WEBサイトから取得したファイルをエクセルで加工してWEBサイトにアップロードするまでを全てPythonで開発したりと、現在も学習及び開発を行っています。"
    aboutMe5="2021年6月からセーブポイントを東京に変更と同時に、IT企業に入社し、7月から案件に出征中です。"
    aboutMe6="尚、前の職場の先輩から「自由にさせると本領発揮するタイプ」と評価されました"


    # 好きと嫌い
    LikeHate_img="static/img/LikeAndHate.jpg"
    LikeHate0="好きな物は、たまご料理、挑戦やリベンジ、コーディング、海外"
    LikeHate1="挑戦について、留学中に国内のインターネットが使用不可、地図は未所持という状態になり、セーブポイント(寮)まで数十kmありました。"
    LikeHate2="残り数時間で帰還出来なければ野宿を覚悟し、野生の勘と進んだ方向を頼りに進んだ結果、帰還出来ました。"
    LikeHate3="その冒険により、未知に挑戦する際の脳内報酬系による興奮と、成功体験によって生成されたドーパミンの獲得でした。"
    LikeHate4="この冒険の体験は現場でも、初めて確認されたエラーが表示された際や、PCキッティングの手順の効率化を図る際も同様に、常に興奮しつつ業務を行っています。"
    LikeHate5="苦手な物は、運動、非合理的な対処、待機、人に関心を持つ事"
    LikeHate6="人に関心を持つ事について、指示を頂いたり、目に余る事がない限りは、自分の業務に全集中するので干渉しません。人間関係のトラブル回避に役立っており、不要な部分でストレスを感じる事はありません。"
    LikeHate7="と、真面目な事を書きましたが、たまご料理とPCを与えればご機嫌です。るんるんです。"
    LikeHate8="また、留学中に現地の人や観光客に、笑顔で手を振りながら現地語で挨拶をずっと続ける奇行を突然行うことがあります。結果、韓国の観光客の人達と何故か一緒に写真撮ったり、現地のこどもとジェスチャーでコミュニケーションをとったりしていました。"


    # 自由時間
    FreeTime_img="static/img/FreeTime.jpg"
    FreeTime0="休日・平日の余暇時間"
    FreeTime1="出退勤時の移動時間・休憩中は、弊社の対応などのタスクがなければ、英語と開発中のアプリケーション改善方法の考案及び模索を行っています。"
    FreeTime2="具体的には、Pythonで簡易IoTアプリやExcelファイル作成アプリの開発・ラズベリーパイでミニPCを作成・Androidのアプリを完全に終了させる簡易アプリ作成など行っています。"
    FreeTime3="たまに、スマホゲームでモンスターのレベル上げに全集中します。"
    FreeTime4="英語については、教材のIELTS・アメリカ国営放送のVoice Of America・IELTSのInstagramで英語に関するポストの視聴など行っています。"
    FreeTime4="業務でも英文のエラーメッセージが表示された際に、早押しクイズ並に即答したり、メンバーから何が書いているのか教えてほしいとの依頼を頂いた際に、その場で確認してお伝えしています。"
    FreeTime5="と書きましたが、突然散歩という名の冒険に出かけたりします。雲ひとつない青空を見ると、自転車をひたすら漕ぎたくなります。さながらハムスターです。滑車回します。"


    # 興味のあるニュース
    News_img="static/img/News.png"
    News0="興味があるニュース"
    News1="Amazonが無人機による配送・販売を行なっている事です。"
    News2="2022年6月 アメリカのロックフォードにテスト導入されますが、この街は小さく、畜産や農業をしている住民が多いので地域住民からは歓迎されておらず、秘密裏に計画実行されたので6月に知らされたとの記事を見ました。"
    News3="昨今、「AIが仕事を奪う」といわれていますが、仕事があまりない田舎町から更に仕事を奪った後、人々はどのような反応や行動を起こすのか興味があります。"
    News4="また、2018年にAmazon Goというレジ・販売員がいない店舗の導入をアメリカのシアトルで開始しましたが、そのAmazonの技術レベルの高さに興味があります。"
    News5="しかし、ハッキングを行う団体に狙われた際、セキュリティホールが人工的に作られる事の防止や、クラッキングを行われた際の対策や修復などを、どのようにしているのか興味があります。"
    News6="最近あったことは、"


    # ポートフォリオ
    portf_img="static/img/portfolio.jpg"
    portf0="ポートフォリオ"
    portf1="鬱対策アプリ"
    portf2="入力された悩みから、sklearnのアルゴリズムを使用し、段階的に解決方法を提案します。"
    portf3="「A」でログインして頂ければ、中身を確認できます。"
    portf4="Click here"
    portf5="ここをクリック"
    portf6="Klicka här."
    portf7="Cliquez ici."


    # 使用経験SW
    SFex_img="static/img/SFex.gif"
    SFex0="使用経験のあるソフトウェア・フレームワーク等"
    SFex1="使用経験のあるソフトウェア・フレームワーク・メソッドと、言語の学習履歴を記載しました。"
    SFex2="Python"
    SFex3="Flask flask-paginate Flask-SocketIO Flask-WTF Django scikit-learn numpy pandas slack-bolt selenium openpyxlなど"
    SFex4="HTMLとCSS JS、PHP データベース"
    SFex5="Laravel / ajax Foundation Bootstrap / MySQL PostgreSQL Heroku など"
    SFex6="英語"
    SFex7="2019年10月〜2020年1月 英語が全くできない状態で、フィリピンにある海外留学に留学。語彙力・発音・リスニングに注力。"
    SFex8="2020年2月〜2021年3月 更なる英語力をつけるため、ECCにてネイティブとのスピーキング・リスニング・ライティング・リーディングを週3通学。"
    SFex9="2021年4月〜 TOEIC スコア655取得。現在は洋書やアメリカのサイトにて勉強中。"
    SFex10="言語学習履歴"
    SFex11="HTML/CSS、JS"
    SFex12="2010年〜2013年 高校在学中に、独学でHTMLとCSSを学習。"
    SFex13="2019年10月〜 海外留学にて、HTML/CSSの基礎・フレームワーク、JSの基礎・ajaxを学習。サーバーにアップする際に、未経験の技術を試行。"
    SFex14="PHP"
    SFex15="2019年10月〜2020年1月 主なバックエンドの動き(フロントからデータを受け取り、バックで加工し、SQLへCRUD指示まで)を学習。"
    SFex16="Python"
    SFex17="2020年3月〜 独学で基礎、web系フレームワーク、アルゴリズム・統計学を学習。現在は自然言語処理を学習しつつ、WEBサイトから取得したcsvファイルをエクセルで加工してWEBサイトにアップロードするまでを全てPythonで開発しました。"
    SFex18="インフラ系"
    SFex19="OTRS ISMCloudone TerioCloud WSS SolitonKeyMagager MS365 mobiconnect / VBBS SymantecEndpointProtection McAfee / CiscoAnyConnect VMwareSSL-VPN TeamViewer など"


    # 保有資格
    certifi_img="static/img/certifications.jpg"
    certifi0="保有資格"
    certifi1="2021年4月 TOEIC公開テスト スコア655取得"
    certifi2="2018年6月 日本商工会議所及び各地商工会議所主催 日商簿記 ３級"
    certifi3="2016年12月 介護職員初任者研修"
    certifi4="2012年12月 日本情報処理検定協会 ホームページ作成検定 １級"
    certifi5="2012年7月 日本情報処理検定協会 表計算 ２級"
    certifi6="2012年3月 全商 パソコン入力スピード認定試験 １級"
    certifi7="2012年2月 日本情報処理検定協会 文書デザイン検定 １級"
    certifi8="2012年1月 全商 プログラミング部門 ２級"
    certifi9="2011年12月 日本情報処理検定協会 プレゼンテーション作成検定 １級"
    certifi10="2011年11月 文部科学省後援秘書技能検定試験 3級"
    certifi11="2011年9月 全商 ビジネス情報部門 ２級"
    certifi12="2011年2月 全商 ビジネス基礎 ３級"
    certifi13="2010年11月 珠算・電卓実務検定 ３級"
    certifi14="2010年9月 全商 情報処理検定 ３級"

    return render_template('index.html',
        css=css,reset_css=reset_css , js=js,

        post0=post0, post1=post1, post_img=post_img,

        aboutMe0=aboutMe0, aboutMe1=aboutMe1, aboutMe2=aboutMe2, 
        aboutMe3=aboutMe3, aboutMe4=aboutMe4, aboutMe5=aboutMe5, aboutMe6=aboutMe6,
        LikeHate0=LikeHate0, LikeHate1=LikeHate1, LikeHate2=LikeHate2, LikeHate3=LikeHate3, LikeHate4=LikeHate4, LikeHate5=LikeHate5, LikeHate6=LikeHate6, LikeHate7=LikeHate7, LikeHate8=LikeHate8, LikeHate_img=LikeHate_img, 

        FreeTime0=FreeTime0, FreeTime1=FreeTime1, FreeTime2=FreeTime2, FreeTime3=FreeTime3,
        FreeTime4=FreeTime4, FreeTime5=FreeTime5, FreeTime_img=FreeTime_img,

        News0=News0, News1=News1, News2=News2, News3=News3,
        News4=News4, News5=News5, News6=News6, News_img=News_img,

        portf0=portf0, portf1=portf1, portf2=portf2, portf3=portf3, portf4=portf4,
        portf5=portf5, portf6=portf6, portf7=portf7,
        portf_img=portf_img,

        SFex0=SFex0, SFex1=SFex1, SFex2=SFex2, SFex3=SFex3, SFex4=SFex4, SFex5=SFex5, SFex6=SFex6, SFex7=SFex7, SFex8=SFex8, SFex9=SFex9, SFex10=SFex10, SFex11=SFex11, SFex12=SFex12, SFex13=SFex13, SFex14=SFex14, SFex15=SFex15, SFex16=SFex16, SFex17=SFex17, SFex18=SFex18, SFex19=SFex19, SFex_img=SFex_img,

        certifi0=certifi0, certifi1=certifi1, certifi2=certifi2, certifi3=certifi3,
        certifi4=certifi4, certifi5=certifi5, certifi6=certifi6, certifi7=certifi7,
        certifi8=certifi8, certifi9=certifi9, certifi10=certifi10,
        certifi11=certifi11, certifi12=certifi12, certifi13=certifi13,
        certifi14=certifi14, certifi_img=certifi_img,
        
        )

@app.route('/more')
def morehello():
    css = "static/style.css"
    reset_css = "static/reset.css"
    js = "static/main.js"
    return render_template('more.html',
        css=css ,reset_css=reset_css , js=js,
        )


if __name__ == "__main__":
    app.run(debug=True)
