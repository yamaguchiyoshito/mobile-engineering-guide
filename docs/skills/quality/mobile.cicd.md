---
title: "CI/CD・静的解析"
description: "CI/CD・静的解析の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# CI/CD・静的解析

**要素技術ID：** `mobile.cicd`  
**技術領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** チーム開発、ビルドと依存管理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

コードの変更をリポジトリに送るたびに、ビルド、テスト、コードの書き方の自動検査（静的解析）、テスト配信などを自動で実行する仕組みを作り、運用する技術です。モバイルアプリはiOSのビルドにmacOSの環境が必要で、配布には署名情報も扱うため、Webやサーバーの開発に比べてビルド環境の準備と秘密情報の受け渡しに手間がかかります。最初に押さえるのは、ワークフロー（パイプライン）が「いつ」「どの環境で」「どの手順を」実行するかの定義であることと、失敗したときにログから原因の手順を特定する読み方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

継続的インテグレーション、自動ビルド、静的解析、自動配布の目的と違いを説明できず、パイプラインの結果確認に手順ごとの指示が必要である。

## Lv1

既存のパイプラインを実行し、失敗したジョブのログから該当箇所を確認できる。静的解析の指摘は支援を受けて修正できる。

## Lv2

変更ごとにビルド、静的解析、書式検査、単体テストを実行するワークフローを構成し、失敗時に原因を特定して修正できる。依存関係とビルド成果物のキャッシュを設定し、実行時間と結果を確認できる。

## Lv3

複数プラットフォームのビルド、署名情報の安全な受け渡し、UIテスト、配布までを含むパイプラインを設計できる。実行環境の費用と待ち時間、不安定なジョブ、静的解析規則の過不足を分析し、段階の分割や並列化で改善できる。

## Lv4

共通のパイプライン定義、静的解析と書式の規約、署名管理、失敗時の対応手順をチームの標準として整備できる。他者の利用実績を基に、ビルド時間、不安定な失敗、レビューでの指摘件数、リリースまでのリードタイムが改善したことを確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントに沿って、プッシュのたびに自分のアプリのビルドと単体テストを実行するワークフローを作る。テストをわざと失敗させ、ログから該当箇所を見つける | [GitHub Actions](https://docs.github.com/ja/actions)・[Pro Git（日本語）](https://git-scm.com/book/ja/v2) |
| Lv2 | 小さなアプリのリポジトリに、プルリクエストごとにビルド、静的解析（SwiftLint、ktlint、ESLintなど）、書式検査、単体テストを実行するワークフローを構成する。依存関係のキャッシュを設定し、設定前後の実行時間を比べる | [GitHub Actions](https://docs.github.com/ja/actions)・[GitHub Pull Request](https://docs.github.com/ja/pull-requests)・[Gradleビルド](https://developer.android.com/build) |
| Lv3 | 既存のパイプラインに、署名情報を安全に受け渡して配布用ビルドを作成し、テスト配信まで行う段階を追加する。ジョブの実行時間と不安定な失敗を集計し、段階の分割や並列化で待ち時間を短くする | [fastlane](https://docs.fastlane.tools/)・[Xcode Cloud](https://developer.apple.com/xcode-cloud/)・[Expo EAS](https://docs.expo.dev/eas/)・[GitHub Actions](https://docs.github.com/ja/actions) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| ワークフローの実行環境 | GitHub Actions（macOSランナー）、Xcode Cloud | GitHub Actions、Bitrise | EAS BuildのCI連携 |
| ビルドの自動化と高速化 | fastlane | Gradleキャッシュ | EAS Build |
| 静的解析と書式検査 | SwiftLint、SwiftFormat | ktlint、detekt、Android Lint | ESLint／TypeScript検査 |
| テストの自動実行 | xcodebuild test、fastlane scan | Gradle test、connectedAndroidTest | JestのCI実行、DetoxのCI実行 |
| 署名情報の管理 | 署名のCI管理（match等） | Play App Signing、CIのシークレットに保管したkeystore | EASの資格情報管理 |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="github-actions, github-actions-secrets, xcode-cloud, bitrise, eas-build-ci, fastlane-match, fastlane-scan, gradle-build-cache, android-command-line-tests, swiftlint, swiftformat, ktlint, detekt, android-lint, eslint" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [GitHub Actions](https://docs.github.com/ja/actions) | 共通 | リポジトリのイベントを契機にビルドやテストを自動で実行する仕組み |
| 公式リファレンス | [GitHub Actionsのシークレット](https://docs.github.com/ja/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) | 共通 | 署名鍵やトークンをシークレットとして保管しワークフローで使う方法 |
| 公式リファレンス | [Xcode Cloud](https://developer.apple.com/documentation/xcode/xcode-cloud) | iOS | Appleのクラウドでアプリのビルド・テスト・配布を自動化するサービス |
| 公式リファレンス | [Build Cache（Gradle）](https://docs.gradle.org/current/userguide/build_cache.html) | Android | タスクの出力を再利用してGradleビルドの時間を短縮する仕組み |
| 公式リファレンス | [コマンドラインからのテスト（Android）](https://developer.android.com/studio/test/command-line) | Android | Gradleのコマンドで単体テストや実機テストを実行する方法 |
| 公式リファレンス | [Lintによるコードの改善（Android）](https://developer.android.com/studio/write/lint) | Android | Android Lintでコードやリソースの問題を検出する方法 |
| ライブラリ | [Bitrise](https://docs.bitrise.io/en/bitrise-ci) | 共通 | モバイルアプリのビルド・テスト・配布を自動化するCIサービス |
| ライブラリ | [match（fastlane）](https://docs.fastlane.tools/actions/match/) | iOS | 証明書とプロビジョニングプロファイルをチームで共有・管理するツール |
| ライブラリ | [scan（fastlane）](https://docs.fastlane.tools/actions/scan/) | iOS | iOSアプリのテストを実行し結果をレポートにまとめるアクション |
| ライブラリ | [SwiftLint](https://github.com/realm/SwiftLint) | iOS | Swiftのコードを規約に照らして検査する静的解析ツール |
| ライブラリ | [SwiftFormat](https://github.com/nicklockwood/SwiftFormat) | iOS | Swiftのコードを決めた書式に自動で整形するツール |
| ライブラリ | [ktlint](https://github.com/ktlint/ktlint) | Android | Kotlinのコードの書式を検査して自動で整形するツール |
| ライブラリ | [detekt](https://detekt.dev/) | Android | Kotlinのコードの複雑さや問題のある書き方を検出する静的解析ツール |
| ライブラリ | [ESLint](https://github.com/eslint/eslint) | React Native | JavaScriptとTypeScriptのコードの問題を検出する静的解析ツール |
| 学習資料 | [CIからのビルド（React Native）](https://docs.expo.dev/build/building-on-ci/) | React Native | CIサービスからEAS Buildを起動してビルドを自動化する手順 |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
