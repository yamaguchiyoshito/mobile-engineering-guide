# 構成と公開設計

文書の正本は `docs/` のMarkdownです。同じ正本からGitHub Pagesのサイトと単一Markdownを生成します。**公開リポジトリと一般公開のPages** を前提とします。

## ディレクトリごとの責任

| パス | 内容・責任 |
| :--- | :--- |
| `README.md` | 初回登録、公開、ローカル実行の入口 |
| `ARCHITECTURE.md` | ページ構成と生成・公開設計 |
| `CONTRIBUTING.md` / `CHANGELOG.md` | 公開側の編集手順・改訂履歴への入口 |
| `docs/index.md` | 読む順序と目的別の入口 |
| `docs/guide/` | モバイル開発の前提、評価手順、改善方法、学習の進め方、用語集。`learning/` にプラットフォーム別の学習コンテンツ |
| `docs/skills/<領域>/<ID>.md` | 1の要素技術1ファイル、対象プラットフォーム、Lv0〜Lv4、技術の対応表の正本 |
| `docs/checklists/<分野>.md` | 1分野1ファイル、各4項目の正本 |
| `docs/templates/` | 記入説明と空のテンプレートの正本 |
| `docs/examples/` | 架空の記入例 |
| `docs/maintenance/` | 運用・改訂・出典 |
| `docs/downloads.md` | 生成した配布物の入口 |
| `docs/.vitepress/` | サイト設定、ナビゲーション、日本語検索、テーマ |
| `docs/public/assets/` | 公開する静的アセット |
| `docs/public/downloads/` | ビルド時に生成する配布物。Git管理対象外 |
| `build/document-map.json` | 全ページのパス・タイトル・分類・順序。React Nativeの前提となる要素技術の参照先URL |
| `build/references.json` | 関連ライブラリ・参考資料の参照レジストリ（id、名称、URL、種別、対象、概要、確認日） |
| `build/learning-paths.json` | 学習の段階とプラットフォームごとの要素技術の割り当て。学習の進め方と学習コンテンツ3ページの正本 |
| `scripts/` | 構造検査、一覧同期、配布物生成、HTML・ブラウザ検証、タグ検証、外部リンク検査 |
| `.github/workflows/docs.yml` | PR/mainの検査。ルート・サブディレクトリの2構成 |
| `.github/workflows/pages.yml` | 公開タグの検証、ビルド、ブラウザ確認、Pagesへの公開 |
| `.github/workflows/links.yml` | 月1回の外部リンク到達確認。失敗時にIssueを作成 |
| `.github/pull_request_template.md` | 変更理由・評価影響・検証結果の記録 |
| `package.json` / `package-lock.json` | 文書版、実行コマンド、固定した依存関係 |
| `.nvmrc` | 開発・CIで使うNode.jsの版 |
| `dist/` / `artifacts/` | 単一文書と検査結果。Git管理対象外 |
| `claudedocs/` | 構築計画。Git管理対象外 |

## ページ構成

| ページ群 | ページ数 | 入口 |
| :--- | ---: | :--- |
| ホーム | 1 | `docs/index.md` |
| 使い方ガイド | 10 | `docs/guide/mobile-basics.md`（学習コンテンツ3ページを含む） |
| 要素技術一覧 | 1 | `docs/skills/index.md` |
| 領域一覧 | 4 | `docs/skills/<領域>/index.md` |
| 要素技術個別定義 | 34 | `docs/skills/<領域>/<ID>.md` |
| チェックリスト一覧 | 1 | `docs/checklists/index.md` |
| 分野別チェックリスト | 25 | `docs/checklists/<分野>.md` |
| 書式一覧・書式 | 5 | `docs/templates/index.md` |
| 記入例一覧・記入例 | 3 | `docs/examples/index.md` |
| 運用・改訂 | 4 | `docs/maintenance/index.md` |
| ダウンロード | 1 | `docs/downloads.md` |
| **合計** | **89** | 404ページとダウンロードファイルを除く |

全ファイルの対応は `build/document-map.json` で管理します。4領域のディレクトリは `foundation`、`applied-foundation`、`implementation`、`quality` です。要素技術分類に「レベル」は使用せず、習熟度だけをLv0〜Lv4で表します。

## 要素技術の定義の構造

各要素技術のページは、要素技術ID、領域、対象プラットフォーム（共通・iOS・Android・React Native のいずれか）、前提、「この要素技術について」（初学者向けの概要）、Lv0〜Lv4、「次のLvへ進むために」（課題と公式資料）、技術の対応表（用途×プラットフォーム）、関連ライブラリと参考資料（参照レジストリから生成）で構成します。Lv0〜Lv4はプラットフォームに依存しない到達状態として記述し、製品名・API名は技術の対応表に置きます。`docs:check` は対象プラットフォーム行の値と5つのLv定義の存在を検査します。

## チェックリストの構造

25分野は「設計・開発」「品質」「開発・運用」「組織・連携」の4区分に分かれ、各分野は「この分野の背景」（初学者向けの説明）と連続する4項目を持ちます。回答例の固有名詞には初出時に短い補足を付けます。各分野の1〜3項目目は取り組みの実施を問い（望ましい回答TRUE）、4項目目は問題の発生を問います（FALSE）。`docs:check` はこの並びを検査します。68項目はDX Criteriaの原文、32項目は本ガイドで作成したモバイル固有の項目です。区別は `docs/maintenance/sources.md` に記載しています。

## 閲覧経路とURL

- 上部メニュー：使い方、要素技術の定義、チームチェック、書式・記入例、運用・改訂。ダウンロードを補助リンクとして配置。
- サイドバー：開いているページ群に対応。34の要素技術は領域ごと、25分野は4つのまとまりで折りたたむ。
- 初めて読む順序：全体像 → 個人評価 → チーム確認 → 改善 → 詳細定義 → 書式。前後リンクも文書マップから生成。
- 各ページ：見出し目次、版、本文、前後ページへのリンク。
- ページURL：`index.md` は末尾 `/`、他は `.html`。例：`skills/implementation/swiftui.basic.html#lv3`、`checklists/security.html#c029`。
- 原稿中の内部リンクは相対Markdownリンクで記載し、GitHubの閲覧とPagesの両方で辿れるようにする。

## 正本と生成物

`document-map.json` は構造情報のみを持ち、習熟度定義・回答例は各Markdownに一度だけ記載します。一覧の自動生成箇所は `catalog` コメントで区切ります。領域一覧の表は、各要素技術のページの対象プラットフォーム行と前提行から生成します。各要素技術のページの「関連ライブラリと参考資料」の表は、`references` マーカーに列挙した id を `build/references.json` から引いて生成します。1つのURLを1か所で管理し、未定義・未使用の id と件数（1ページ3〜15件）を `docs:check` で検査します。外部リンクの到達確認は `npm run check:links` と月次のワークフローで行い、PRごとの検査には含めません。

学習コンテンツ3ページ（`docs/guide/learning/`）の段階節は、`learning` マーカーの間に `build/learning-paths.json` の割り当てに従って生成します。各要素技術の概要文は「この要素技術について」の第1文、課題表は「次のLvへ進むために」の表、学習資料は参照レジストリの学習資料種別から転記します。`docs:check` は、対象プラットフォームが一致する要素技術が各ページに漏れなく割り当てられていることを検査します。変更時に `docs:sync` を実行し、同期漏れをCIで検出します。

単一Markdownでは、各ページ・見出しに一意のアンカーを生成し、ページ間の参照を文書内参照へ変換します。コードブロック内の記入用見出しは変換しません。全アンカーの存在を生成時に確認します。

書式ダウンロードは各ページの `template` コメント内を抽出します。4書式の個別MarkdownとZIPを生成し、版・コミット・生成日時を添えます。配布マニフェストにはサイズとSHA-256を記録します。

`docs/public/**` はMarkdownページの走査対象から除き、生成した配布Markdownが重複した閲覧ページ・検索結果にならないようにします。

## 技術構成

- VitePress **1.6.4** の安定版と標準テーマを使用。
- Viteは **6.4.3** にoverrideで固定。VitePress既定の旧版に残る開発サーバー関連の既知問題を避け、サイト生成・表示を検証。
- 依存はpackage-lock.jsonに固定し、CIでは `npm ci` を使用。
- 日本語は文字と連続2文字の組で索引化する。Node.jsとブラウザ間の辞書差異を避け、索引側と検索側へ同じtokenize関数を適用する。英数字の区切りは固定し、`swiftui.basic`、`react-native.basic`、`C029`、`029` を保持する。
- 検索はVitePressのローカル検索。外部の検索サービスやAPIキーを使用しない。
- 明暗表示、キーボード操作、モバイル目次・検索に対応。外部フォントや解析タグは追加しない。

## 検査と公開の境界

PRとmainの検査は `contents: read` で実行し、公開権限を持ちません。ルート `/` とプロジェクトパス `/preview-repository/` の両方で、文書の整合、HTMLの参照、検索、ダウンロード、モバイル表示を確認します。

公開ワークフローは `vX.Y.Z` タグを対象とし、タグの形式、package.jsonとの一致、mainへの包含を確認します。ビルドジョブは読み取り権限で動き、成功したPages artifactだけをデプロイジョブが公開します。デプロイジョブにのみ `pages: write` と `id-token: write` を付けます。

公開先のbase pathとoriginはGitHub Pagesの設定から取得します。コードに所有者名を固定しません。同時公開を直列化し、手動再実行では既存のタグを指定して旧版を再公開できます。

GitHub上の設定と最初のpushはREADMEに記載しています。配布時点で特定のGitHubリポジトリへの登録や公開は行っていません。
