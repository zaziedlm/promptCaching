# 走れメロス 分析ツール
このプロジェクトは、OpenAI API を使用して太宰治の小説「走れメロス」を分析するシンプルなデモです。
プロンプトキャッシングが効いているかを検証する目的で実装されました。

## 使い方
- OpenAI API キー: https://platform.openai.com/account/api-keys から API キーを取得する必要があります。  
- `.env-template` ファイルを元にして、`.env`ファイルにこれを配置します。
- 「走れメロス」のテキスト: スクリプトは、hashire_merosu.txt というファイルにテキストがあることを想定しています。  
- Python 3.x: スクリプトは Python 3.x で記述されています。  
これらの前提条件が揃ったら、以下のコマンドを実行してスクリプトを実行できます。

```bash
poetry add openai python-dotenv
 or
pip install openai python-dotenv 
```

```bash
python merosu-promptcaching.py
```

## 注意事項
スクリプトは、入力を求めます。小説に関する質問をすることができ、スクリプトは OpenAI API を使用して応答を生成します。  
プロンプトキャッシングのtoken数を細かく見る意図で、以前の対話メッセージは積み上げせずに、messagesを都度で構築し直しています。

- hashire_merosu-first.txt: 走れメロスの最初の部分のテキスト。  
- hashire_merosu-half.txt: 走れメロスの途中箇所の抜き出し版、途中と最終部分。  

プロンプトキャッシングの効果を見るために、読み込む文章箇所を取り換えながら実行することができます。  
