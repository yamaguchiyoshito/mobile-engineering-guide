---
title: "署名・配布・ストア公開"
description: "署名・配布・ストア公開の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# 署名・配布・ストア公開

**要素技術ID：** `mobile.release`  
**技術領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** ビルドと依存管理

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

作ったアプリを利用者の端末に届けるために、署名、テスト配信、ストアへの提出と審査、公開までを行う技術です。サーバーにデプロイすれば全員に反映されるWebと違い、モバイルアプリは開発者の署名を付けた配布用ビルドをApp StoreやGoogle Playの審査に通し、段階的に公開した後、利用者が端末上でアップデートして初めて新しい版が動きます。そのため公開後すぐに全員へ届くわけではなく、しばらくは旧版を使い続ける利用者が残り、不具合が見つかっても配布済みの版を即座に取り消すことはできません。最初に押さえるのは、署名が「誰が作ったアプリか」を証明する仕組みであることと、公開する利用者の割合を少しずつ広げる段階的公開の考え方です。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

署名、配布用ビルド、テスト配信、ストア審査、公開の違いを説明できず、配布作業の各段階に手順ごとの指示が必要である。

## Lv1

手順書と用意された署名情報を使って配布用ビルドを作成し、テスト配信へアップロードできる。署名エラーや審査の指摘への対応には支援が必要である。

## Lv2

バージョン番号とビルド番号、署名設定、ストア掲載情報、プライバシーに関する申告を準備し、テスト配信から公開まで完了できる。審査基準との適合を事前に確認し、指摘を受けた場合は原因を特定して再提出できる。

## Lv3

段階的公開、テスト対象者の区分、強制更新、配布済みバージョンとの互換性を含むリリース計画を設計できる。審査の遅延、公開後の不具合による配信停止、ストアを経由しない更新の制約などのリスクを比較し、判断の根拠を関係者に説明できる。

## Lv4

署名情報の管理、リリース手順の自動化、公開判定の確認項目、ロールバック方針を整備し、特定の担当者に依存しない体制にできる。他者によるリリース実績を基に、所要時間、審査での差し戻し、公開後の障害対応が改善したことを確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿って自分のアプリの配布用ビルドを作成し、TestFlightまたはGoogle Playの内部テストにアップロードして、自分の端末にインストールできることを確認する | [TestFlight](https://developer.apple.com/testflight/)・[アプリの公開](https://developer.android.com/studio/publish)・[Expo EAS](https://docs.expo.dev/eas/) |
| Lv2 | 小さなアプリについて、バージョン番号とビルド番号の更新、署名設定、スクリーンショットと説明文、プライバシーに関する申告を準備し、審査ガイドラインとの適合を確認したうえでストアへの提出から公開まで完了する | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)・[App Store Connectヘルプ](https://developer.apple.com/help/app-store-connect/)・[アプリの公開](https://developer.android.com/studio/publish)・[アプリ署名](https://developer.android.com/studio/publish/app-signing)・[App Storeへの公開](https://reactnative.dev/docs/publishing-to-app-store)・[署名付きAPK](https://reactnative.dev/docs/signed-apk-android) |
| Lv3 | 既存アプリの次回リリースについて、段階的公開の割合と期間、テスト対象者の区分、旧版とAPIの互換性、強制更新の条件、公開後に不具合が見つかった場合の配信停止の手順を含むリリース計画を作り、関係者に説明する | [App Store Connectヘルプ](https://developer.apple.com/help/app-store-connect/)・[アプリの公開](https://developer.android.com/studio/publish)・[Expo EAS](https://docs.expo.dev/eas/) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 署名と配布用ビルド | 証明書・プロビジョニングプロファイル | アプリ署名（Play App Signing）、AAB | EAS Build |
| テスト配信 | TestFlight | Play Console（内部テスト・クローズド・オープン）、Firebase App Distribution | EAS Buildの内部配布、各ストアのテスト配信 |
| ストア掲載と審査 | App Store Connect、App Review Guidelines、プライバシーマニフェスト、ASO | Play Console、データセーフティ | EAS Submit、ストア公開手順 |
| 段階的な公開と更新 | 段階的リリース | Play Consoleの段階的公開 | EAS Update、OTA更新の制約 |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="apple-certificates, apple-appstore-provisioning, testflight, app-store-connect-help, app-review-guidelines, privacy-manifest, apple-phased-release, play-console, android-app-signing, android-app-bundle, android-data-safety, firebase-app-distribution, eas-build, eas-submit, eas-update" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [証明書の概要（iOS）](https://developer.apple.com/help/account/certificates/certificates-overview/) | iOS | 開発と配布に使う署名用証明書の種類と作成方法の解説 |
| 公式リファレンス | [App Storeプロビジョニングプロファイル（iOS）](https://developer.apple.com/help/account/provisioning-profiles/create-an-app-store-provisioning-profile/) | iOS | App Store配布用のプロビジョニングプロファイルを作成する手順 |
| 公式リファレンス | [TestFlight](https://developer.apple.com/testflight/) | iOS | ベータ版のアプリをテスターに配布してフィードバックを集める仕組み |
| 公式リファレンス | [App Store Connectヘルプ（iOS）](https://developer.apple.com/help/app-store-connect/) | iOS | アプリの登録・提出・配信管理の手順をまとめたヘルプ |
| 公式リファレンス | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | iOS | App Storeの審査で確認される安全性や内容などの基準 |
| 公式リファレンス | [プライバシーマニフェスト（iOS）](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) | iOS | アプリやSDKが収集するデータと使用するAPIの理由を記述するファイル |
| 公式リファレンス | [段階的リリース（iOS）](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases) | iOS | アップデートを7日間かけて自動更新の利用者へ段階的に配信する手順 |
| 公式リファレンス | [Google Play Console](https://developer.android.com/distribute/console) | Android | Google Playでのアプリ公開・テスト配信・段階的公開を管理する画面 |
| 公式リファレンス | [アプリへの署名（Android）](https://developer.android.com/studio/publish/app-signing) | Android | APKやAABに署名してリリース用の成果物を作る手順 |
| 公式リファレンス | [Android App Bundle](https://developer.android.com/guide/app-bundle) | Android | 端末ごとに最適化したAPKを配信するためのアップロード形式 |
| 公式リファレンス | [データの使用の申告（Android）](https://developer.android.com/privacy-and-security/declare-data-use) | Android | Google Playのデータセーフティ欄にデータの収集・共有を申告する方法 |
| 公式リファレンス | [EAS Build](https://docs.expo.dev/build/introduction/) | React Native | Expoのクラウド環境でAndroidとiOSのアプリをビルドするサービス |
| ライブラリ | [Firebase App Distribution](https://firebase.google.com/docs/app-distribution) | iOS・Android | リリース前のアプリをテスターに配布してフィードバックを集めるサービス |
| ライブラリ | [EAS Submit](https://docs.expo.dev/deploy/submit-to-app-stores/) | React Native | ビルドしたアプリをApp StoreとGoogle Playへ提出するサービス |
| ライブラリ | [EAS Update](https://docs.expo.dev/eas-update/introduction/) | React Native | ストア審査を経ずにJavaScriptと画像などの更新を配信するサービス |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
