# モバイルアプリ開発ガイド

一般公開のGitHub Pagesで読む、iOS・Android・React Nativeアプリ開発のスキル評価とチーム改善の文書です。

- 4つのスキル領域、34スキル、Lv0〜Lv4の170定義。各スキルに対象プラットフォーム（共通、iOS、Android、React Native）と技術の対応表
- 25分野、100チェック項目、原文・望ましい判定・回答例
- 評価手順、4種類の空の書式、架空の記入例
- 82ページ、日本語全文検索、単一Markdownと書式のダウンロード

まず [ガイドの全体像](docs/guide/overview.md) を読み、[スキル定義](docs/skills/index.md)・[チームチェック](docs/checklists/index.md) を参照してください。詳細な構成は [ARCHITECTURE.md](ARCHITECTURE.md)、実行した検証は [VALIDATION.md](VALIDATION.md) に記載しています。スキル体系の出典は [出典と追加した内容](docs/maintenance/sources.md) にあります。

## ローカルで読む

Node.js **24.19.0**（`.nvmrc`）、Python **3.12以降**を使用します。

```bash
npm ci
npm run docs:dev
```

表示されたローカルURLの `/mobile-engineering-guide/` を開きます。ホスト名やリポジトリ名をソースに書き込む必要はありません。

## GitHubへ初回登録する

1. GitHubで、任意の所有者の下に **Public** リポジトリを新規作成します。推奨名は `mobile-engineering-guide` です。README等の初期ファイルは作成しません。
2. このフォルダー内で次を実行します。`YOUR_OWNER` は実際のアカウント・組織名に置き換えてください。

```bash
git remote add origin https://github.com/YOUR_OWNER/mobile-engineering-guide.git
git push -u origin main
```

3. **Settings → Pages → Build and deployment → Source** で **GitHub Actions** を選択します。
4. **Settings → Environments → github-pages** の公開元制限を確認します。制限する場合は、タグの `v*` を許可します。`main` だけの許可ではタグ公開が止まります。
5. **Validate documentation** の検査成功を確認して、初回公開タグをpushします。

```bash
git tag -a v1.0.0 -m "Release public guide 1.0.0"
git push origin v1.0.0
```

**Publish GitHub Pages** がビルド・ブラウザ検証後に公開します。公開URLはActionsのdeploymentまたはSettings → Pagesに表示されます。標準URLは `https://YOUR_OWNER.github.io/mobile-engineering-guide/` です。

React Native の前提スキルへの参照先（`build/document-map.json` の `frontendGuide.url` と `docs/skills/implementation/react-native.basic.md` のリンク）に含まれる `YOUR_OWNER` も、フロントエンド領域のガイドを公開した所有者名に置き換えてください。

GitHub Freeでは公開リポジトリからPagesを公開できます。公開サイトにログインは不要です。[公式仕様](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

## 検査と生成

```bash
npm run docs:sync
npm run docs:build
npx playwright install --with-deps chromium
npm run test:site
npm run docs:preview
```

| コマンド | 処理 |
| :--- | :--- |
| `docs:sync` | 文書マップから一覧ページのリンク・表を同期 |
| `docs:check` | 82ページ、34スキル、170定義、100項目、判定、対象プラットフォーム、内部参照を検査 |
| `docs:downloads` | 単一Markdown、空の4書式、ZIP、生成元・SHA-256を生成 |
| `docs:build` | 文書検査・ダウンロード生成・サイトビルド |
| `test:site` | 生成HTMLの参照検査と、Chromiumによる表示・検索・ダウンロード確認 |
| `test:release` | 公開タグ検証の単体テスト |

## 構成の由来

評価手順、判定ルール、記録書式、サイトの生成・公開の仕組みは、同じ形式のフロントエンド領域のガイドと共通です。スキル体系は roadmap.sh の iOS、Android、React Native、SwiftUI のロードマップを参照して構成しています。詳細は [出典と追加した内容](docs/maintenance/sources.md) を参照してください。
