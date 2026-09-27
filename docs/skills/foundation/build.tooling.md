---
title: "ビルドと依存管理"
description: "ビルドと依存管理の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# ビルドと依存管理

**要素技術ID：** `build.tooling`  
**技術領域：** [基礎領域](index.md)  
**対象プラットフォーム：** 共通  
**評価対象：** ビルド設定、依存関係の追加・更新、成果物の生成

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

書いたコードと外部のライブラリを組み合わせ、端末にインストールできる形（成果物）にまとめる仕組みを扱います。Webの開発でもライブラリの追加やビルドは行いますが、モバイルアプリではiOS向けとAndroid向けでビルドの仕組みが異なり、ストアに提出する成果物には署名が必要です。また、開発用とリリース用などのビルド構成の違いが、そのまま利用者の手元のアプリの動作に表れます。最初に押さえるのは、アプリが使う外部ライブラリとそのバージョン（依存関係）を管理ツールに宣言して取り込む考え方と、同じコードから複数の構成の成果物を作り分けられることです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

ビルド設定、依存関係、成果物の関係を説明できず、ライブラリの追加やビルドに手順ごとの指示が必要である。

## Lv1

手順書に沿って依存ライブラリを追加し、指定された構成でビルドして成果物を生成できる。依存の競合やビルド設定の変更が必要な場合に支援を求められる。

## Lv2

要件に合わせて依存ライブラリを選定・追加・更新し、開発用とリリース用などのビルド構成を使い分けられる。ビルドエラーや依存の不整合を解消し、生成した成果物が意図した構成であることを確認できる。

## Lv3

推移的な依存の競合、更新による互換性の破壊、ビルド時間の増大などを分析し、原因を特定して改善できる。依存の導入可否やモジュール分割の案を保守性、ビルド時間、成果物サイズの観点で比較し、他者の変更をレビューできる。

## Lv4

依存管理とビルド構成の標準、共通設定、依存更新の自動検証を整備できる。他者の利用実績から、ビルド失敗や依存更新にかかる工数の変化を確認し、仕組みを更新できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿って、画像の読み込みやHTTP通信などに使う外部ライブラリを1つ追加し、アプリから呼び出してビルド・実行する。開発用の構成で成果物を生成し、その保存場所を確認する | [Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages)・[Gradleビルド](https://developer.android.com/build)・[Expoドキュメント](https://docs.expo.dev/) |
| Lv2 | 開発用とリリース用でAPIの接続先とアプリの表示名が切り替わるようにビルド構成を分け、両方の成果物を生成して、実際に切り替わっていることを確認する。依存ライブラリを1つ更新し、ビルドと動作に問題がないことを確かめる | [Xcode](https://developer.apple.com/documentation/xcode)・[Gradleビルド](https://developer.android.com/build)・[Expo EAS](https://docs.expo.dev/eas/) |
| Lv3 | 既存プロジェクトの依存関係を一覧にし、同じライブラリの異なるバージョンが間接的に入り込んでいる箇所や、ビルド時間の多くを占める工程を調べる。ライブラリを使い続ける案と置き換える案を、保守性、ビルド時間、成果物サイズの観点で比べる | [Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages)・[Gradleビルド](https://developer.android.com/build)・[Expo EAS](https://docs.expo.dev/eas/) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 依存ライブラリの管理 | Swift Package Manager、CocoaPods、Carthage | バージョンカタログ | npm／yarn、autolinking |
| ビルド構成の切り替え | ビルド設定（Configuration） | Build Variant | app.config、EAS Buildのプロファイル |
| ビルドの実行 | xcodebuild | Gradle（Kotlin DSL） | Expoプレビルド、EAS Build |
| 成果物の生成と最適化 | xcframework | R8、署名付きAPK／AAB | Hermes |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="swift-packages, cocoapods, carthage, xcode-build-config-file, xcode-xcframework, android-version-catalogs, android-build-variants, android-kotlin-dsl, android-app-optimization, android-app-signing, expo-app-config, expo-autolinking, expo-cng, eas-build, rn-hermes" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Swift packages](https://developer.apple.com/documentation/xcode/swift-packages) | iOS | Swift Package Managerでコードを分割・共有する方法 |
| 公式リファレンス | [ビルド設定ファイルの追加（iOS）](https://developer.apple.com/documentation/xcode/adding-a-build-configuration-file-to-your-project) | iOS | xcconfigファイルで構成ごとのビルド設定を管理する方法 |
| 公式リファレンス | [マルチプラットフォームのバイナリフレームワーク作成（iOS）](https://developer.apple.com/documentation/xcode/creating-a-multi-platform-binary-framework-bundle) | iOS | xcodebuildでXCFrameworkを作成し配布する方法 |
| 公式リファレンス | [バージョンカタログへの移行（Android）](https://developer.android.com/build/migrate-to-catalogs) | Android | 依存ライブラリのバージョンを一か所で管理する方法を説明 |
| 公式リファレンス | [ビルドバリアントの設定（Android）](https://developer.android.com/build/build-variants) | Android | ビルドタイプとフレーバーで成果物を切り替える方法 |
| 公式リファレンス | [Kotlin DSLへの移行（Android）](https://developer.android.com/build/migrate-to-kotlin-dsl) | Android | GradleのビルドスクリプトをKotlin DSLで書く方法を説明 |
| 公式リファレンス | [アプリの最適化（Android）](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) | Android | R8によるコードの縮小と難読化を有効にする方法を説明 |
| 公式リファレンス | [アプリへの署名（Android）](https://developer.android.com/studio/publish/app-signing) | Android | APKやAABに署名してリリース用の成果物を作る手順 |
| 公式リファレンス | [アプリの設定（React Native）](https://docs.expo.dev/workflow/configuration/) | React Native | app.jsonやapp.config.jsでアプリの設定を記述する方法 |
| 公式リファレンス | [Expo Autolinking](https://docs.expo.dev/modules/autolinking/) | React Native | インストールしたネイティブモジュールを自動で組み込む仕組み |
| 公式リファレンス | [Continuous Native Generation（React Native）](https://docs.expo.dev/workflow/continuous-native-generation/) | React Native | prebuildで設定からネイティブプロジェクトを生成する仕組み |
| 公式リファレンス | [EAS Build](https://docs.expo.dev/build/introduction/) | React Native | Expoのクラウド環境でAndroidとiOSのアプリをビルドするサービス |
| 公式リファレンス | [Hermes](https://reactnative.dev/docs/hermes) | React Native | React Native向けに最適化されたJavaScriptエンジン |
| ライブラリ | [CocoaPods](https://github.com/CocoaPods/CocoaPods) | iOS | Xcodeプロジェクトの依存ライブラリを管理するツール |
| ライブラリ | [Carthage](https://github.com/Carthage/Carthage) | iOS | 依存ライブラリをバイナリのフレームワークとして構築するツール |

<!-- references:end -->

roadmap.shで学ぶ：[iOS](https://roadmap.sh/ios)（Swift Package Manager、CocoaPods、Carthage、Dependency Manager、XCFramework、Static Library、Dynamic Library、Frameworks & Library）／[SwiftUI](https://roadmap.sh/swift-ui)（Creating Packages、Using Packages、Swift Package Index）／[Android](https://roadmap.sh/android)（What Is and How to Use Gradle、Signed APK）／[React Native](https://roadmap.sh/react-native)（Expo、React Native CLI、Create Expo App、Speeding up Builds）

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
