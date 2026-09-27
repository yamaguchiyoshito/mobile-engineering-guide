---
title: "学習の進め方"
description: "学習の進め方の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# 学習の進め方

モバイルアプリ開発に不慣れな人が、担当するプラットフォームごとに34の要素技術をどの順で学ぶかの目安です。段階ごとに到達目安のLvを示します。目安であり、担当業務によって順序と目標は変わります。

各要素技術のページの「この要素技術について」で概要を、「次のLvへ進むために」で課題と参考資料を確認してください。roadmap.shの学習ロードマップ（[iOS](https://roadmap.sh/ios)、[Android](https://roadmap.sh/android)、[React Native](https://roadmap.sh/react-native)、[SwiftUI](https://roadmap.sh/swift-ui)）も併せて参照できます。

## 段階の考え方

| 段階 | 目的 | 到達目安 |
| :--- | :--- | :--- |
| 1.最初の1か月 | 開発環境を整え、言語の基本と画面の作り方を覚え、小さなアプリを動かす。 | 対象の要素技術でLv1 |
| 2.基本を固める | 通信、保存、画面遷移、テストを含む小さなアプリを自力で完成させる。 | 主要要素技術でLv2 |
| 3.実務で広げる | 既存アプリの保守、性能・セキュリティ・配布・監視を担当し、設計判断に関わる。 | 担当領域でLv2〜Lv3 |

どの段階でも、[Git](../skills/foundation/git.basic.md)と[チーム開発](../skills/applied-foundation/git.collaboration.md)は並行して使います。

## iOS

| 段階 | 学ぶ要素技術 |
| :--- | :--- |
| 1.最初の1か月 | [モバイルプラットフォーム基礎](../skills/foundation/mobile.basic.md)、[開発環境](../skills/foundation/ide.basic.md)、[Swift](../skills/foundation/swift.basic.md)、[SwiftUI](../skills/implementation/swiftui.basic.md)、[UIデザイン原則とローカライズ](../skills/applied-foundation/mobile.ui-design.md) |
| 2.基本を固める | [Swift並行処理とメモリ管理](../skills/applied-foundation/swift.concurrency.md)、[ネットワーク通信](../skills/applied-foundation/mobile.networking.md)、[データ永続化](../skills/applied-foundation/mobile.persistence.md)、[画面遷移とディープリンク](../skills/implementation/mobile.navigation.md)、[入力とバリデーション](../skills/implementation/mobile.input-validation.md)、[ビルドと依存管理](../skills/foundation/build.tooling.md)、[ユニットテスト](../skills/quality/test.unit.md) |
| 3.実務で広げる | [UIKit](../skills/implementation/uikit.basic.md)、[リアクティブプログラミング](../skills/applied-foundation/reactive.basic.md)、[アプリアーキテクチャと依存性注入](../skills/implementation/mobile.architecture.md)、[API連携とデータフロー](../skills/implementation/mobile.api-integration.md)、[アクセシビリティ](../skills/applied-foundation/mobile.accessibility.md)、[プラットフォーム機能連携](../skills/implementation/mobile.platform-services.md)、[アニメーションとインタラクション](../skills/implementation/mobile.animation.md)、品質・高度化領域の各要素技術 |

既存アプリの多くはUIKitで書かれています。保守を担当する場合は、段階2でUIKitを先に学びます。

## Android

| 段階 | 学ぶ要素技術 |
| :--- | :--- |
| 1.最初の1か月 | [モバイルプラットフォーム基礎](../skills/foundation/mobile.basic.md)、[開発環境](../skills/foundation/ide.basic.md)、[Kotlin](../skills/foundation/kotlin.basic.md)、[Jetpack Compose](../skills/implementation/compose.basic.md)、[UIデザイン原則とローカライズ](../skills/applied-foundation/mobile.ui-design.md) |
| 2.基本を固める | [Kotlinコルーチン・Flow](../skills/applied-foundation/kotlin.coroutines.md)、[ネットワーク通信](../skills/applied-foundation/mobile.networking.md)、[データ永続化](../skills/applied-foundation/mobile.persistence.md)、[画面遷移とディープリンク](../skills/implementation/mobile.navigation.md)、[入力とバリデーション](../skills/implementation/mobile.input-validation.md)、[ビルドと依存管理](../skills/foundation/build.tooling.md)、[ユニットテスト](../skills/quality/test.unit.md) |
| 3.実務で広げる | [Android Views・Fragment](../skills/implementation/android.views.md)、[リアクティブプログラミング](../skills/applied-foundation/reactive.basic.md)、[アプリアーキテクチャと依存性注入](../skills/implementation/mobile.architecture.md)、[API連携とデータフロー](../skills/implementation/mobile.api-integration.md)、[アクセシビリティ](../skills/applied-foundation/mobile.accessibility.md)、[プラットフォーム機能連携](../skills/implementation/mobile.platform-services.md)、[アニメーションとインタラクション](../skills/implementation/mobile.animation.md)、品質・高度化領域の各要素技術 |

Androidは端末とOSバージョンの幅が広いため、段階2から[端末・OS互換性とサポート方針](../checklists/device-compatibility.md)のチェック項目も参照します。

## React Native

React Nativeでは、JavaScript、TypeScript、Reactの基礎を先に習得します。これらは本書の対象外で、フロントエンド領域の基準で確認します。

| 段階 | 学ぶ要素技術 |
| :--- | :--- |
| 1.最初の1か月 | [モバイルプラットフォーム基礎](../skills/foundation/mobile.basic.md)、[開発環境](../skills/foundation/ide.basic.md)、[React Native実装](../skills/implementation/react-native.basic.md)、[UIデザイン原則とローカライズ](../skills/applied-foundation/mobile.ui-design.md) |
| 2.基本を固める | [ネットワーク通信](../skills/applied-foundation/mobile.networking.md)、[データ永続化](../skills/applied-foundation/mobile.persistence.md)、[画面遷移とディープリンク](../skills/implementation/mobile.navigation.md)、[入力とバリデーション](../skills/implementation/mobile.input-validation.md)、[ビルドと依存管理](../skills/foundation/build.tooling.md)、[ユニットテスト](../skills/quality/test.unit.md) |
| 3.実務で広げる | [React Nativeのネイティブ連携](../skills/implementation/react-native.native-integration.md)、[Swift](../skills/foundation/swift.basic.md)または[Kotlin](../skills/foundation/kotlin.basic.md)の基礎、[アプリアーキテクチャと依存性注入](../skills/implementation/mobile.architecture.md)、[API連携とデータフロー](../skills/implementation/mobile.api-integration.md)、[プラットフォーム機能連携](../skills/implementation/mobile.platform-services.md)、[性能・メモリ・起動時間](../skills/quality/mobile.performance.md)、品質・高度化領域の各要素技術 |

## 品質・高度化領域の学び方

段階3以降で、担当に応じて次の順で広げます。

1. [テスト設計](../skills/quality/test.design.md)と[UIテスト・E2E](../skills/quality/test.ui.md)：小さなアプリに自動テストを追加する。
2. [署名・配布・ストア公開](../skills/quality/mobile.release.md)と[CI/CD・静的解析](../skills/quality/mobile.cicd.md)：テスト配布までを自動化する。
3. [監視・クラッシュ分析](../skills/quality/mobile.observability.md)と[性能・メモリ・起動時間](../skills/quality/mobile.performance.md)：配布後の状態を把握し改善する。
4. [モバイルセキュリティ](../skills/quality/mobile.security.md)：秘密情報の扱い、通信の保護、依存関係の脆弱性に対応する。

## 学習の記録

段階ごとに[個人の習熟度評価記録](../templates/individual-assessment.md)へ、取り組んだ課題、確認した結果、支援を受けた範囲を残します。[記入例：Swiftを学び始めた担当者の個人評価](../examples/individual-swift-lv1.md)に、学習初期の記録の書き方を示しています。
