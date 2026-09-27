---
title: "出典と追加した内容"
description: "出典と追加した内容の基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# 出典と追加した内容

本書は、モバイルアプリ開発の学習ロードマップと、チームの取り組みを問うチェックリストを基に、スキル習熟度の定義、望ましい回答例、評価手順、改善への接続、記録書式を追加したものです。

[スキル定義](../skills/index.md)は、34スキルのID・分類・前提・対象プラットフォームと、各スキルのLv0〜Lv4を収録しています。[チームチェックリスト](../checklists/index.md)は、25分野・100項目を収録しています。各項目のリンクは原文または本書で参照した公式資料です。本書で追加した判定方法や回答例を、リンク先が定める公式の評価方法として扱いません。

PRはPull Requestを指します。GitLabを使用する場合は、MR（Merge Request）に読み替えてください。

## スキル定義の由来

スキルの分類と評価対象は、roadmap.shが公開する次の学習ロードマップのトピックを参照して構成しています。各スキルページの「技術の対応」に、参照したロードマップへのリンクと主なトピック名を記載しています。「次のLvへ進むために」の参考資料は、Apple、Google、React Native、Expo 等の公式資料へのリンクです（到達確認日：2026年9月28日）。

- [iOS Developer Roadmap](https://roadmap.sh/ios)
- [Android Developer Roadmap](https://roadmap.sh/android)
- [React Native Roadmap](https://roadmap.sh/react-native)
- [SwiftUI Roadmap](https://roadmap.sh/swift-ui)

ロードマップは学習順序を示す資料であり、習熟度の判定基準を定めるものではありません。Lv0〜Lv4の到達状態、前提の設定、対象プラットフォームの区分は本書で追加した内容です。サーバーサイドSwiftやエディタの選択など、モバイルアプリ開発の評価に直接関係しないトピックは対象外としています。

React Nativeの前提となるJavaScript、TypeScript、Reactの習熟度は本書に含めていません。別途、フロントエンド領域の基準で確認してください。

## チェックリストの由来

100項目のうち68項目（17分野）は、日本CTO協会が公開するDX Criteriaの項目を原文として収録し、各項目の「原文の参照先」から出典を確認できます。原文中の「フロントエンド」「Webフロントエンド」は、本書ではモバイルアプリ開発チームとその技術領域に読み替えて使用します。原文自体は変更していません。

残る32項目（8分野）は、モバイルアプリ開発に固有の取り組みとして本書で作成した項目です。対象は次の分野です。

| 項目No. | 分野 | 主な参照先 |
| :--- | :--- | :--- |
| 009〜012 | UI部品と画面設計の再利用 | Apple Human Interface Guidelines、Material Design、SwiftUI、Jetpack Compose、React Native |
| 021〜024 | アプリ性能と起動時間 | Apple Xcode・MetricKit、Android vitals、React Native |
| 025〜028 | モバイルアクセシビリティ | Apple Accessibility、Android Accessibility、React Native、WCAG 2.2 |
| 029〜032 | モバイルセキュリティ | OWASP MASVS・MASTG、Apple Keychain、Android Keystore |
| 033〜036 | 権限とプライバシー | App Tracking Transparency、プライバシーマニフェスト、Android権限、Playデータセーフティ |
| 049〜052 | 署名・配布・ストア審査 | TestFlight、App Review Guidelines、Play Console、Android App Signing、Expo EAS |
| 065〜068 | 端末・OS互換性とサポート方針 | App Store利用状況、Android互換性、Firebase Test Lab |
| 069〜072 | オフラインと同期 | Androidオフラインファースト、WorkManager、iOS Background Tasks、NWPathMonitor |

これらの項目の「原文の参照先」は、項目の趣旨に関係する公式資料へのリンクであり、参照先が項目の文面を定めているものではありません。

## 文書の由来

- 習熟度の定義、望ましい回答例、評価手順、改善方法、記録書式は本ガイドで追加した内容です。
- 参照先の更新を自動反映する仕組みではありません。変更時は原文との違いを確認し、改訂履歴へ記載します。
- 評価手順、判定ルール、記録書式、サイトの生成・公開の仕組みは、同じ形式のフロントエンド領域のガイドと共通です。

## 公開方式の公式資料

仕様確認日：2026年9月28日。

- [GitHub Pagesの概要](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Actionsを使ったPages公開](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [VitePress 1系のデプロイ](https://vuejs.github.io/vitepress/v1/guide/deploy)
- [VitePress 1系のサイト内検索](https://vuejs.github.io/vitepress/v1/reference/default-theme-search)

GitHub Freeでも公開リポジトリからGitHub Pagesを公開できます。本実装は公開リポジトリと一般公開サイトの組み合わせを採用し、Enterprise固有機能を使用しません。
