---
title: "用語集"
description: "用語集の基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# 用語集

本書の要素技術の定義、チェックリスト、回答例に出てくる用語を、モバイルアプリ開発に不慣れな人向けに説明します。iOSとAndroidで対応する概念は並べて示します。サイトの検索欄に用語を入力すると、このページと使われているページを探せます。

## プラットフォームと配布

| 用語 | 説明 |
| :--- | :--- |
| ネイティブアプリ | 各OSの言語とフレームワーク（iOSならSwift、AndroidならKotlin）で作るアプリ。React NativeもネイティブのUI部品を描画するため、動作はネイティブアプリに近い。 |
| ストア | アプリを配布する場所。iOSはApp Store、AndroidはGoogle Play。配布前に審査がある。 |
| 審査（ストア審査） | ストアがガイドラインに沿ってアプリを確認する工程。差し戻されると公開が遅れる。 |
| 段階的公開 | 一部の利用者から順に新バージョンを配布する仕組み。問題があれば途中で停止できる。iOSでは「段階的リリース」、Google Playでは「段階的公開」と呼ぶ。 |
| TestFlight／内部テスト | 公開前にテスト参加者へ配布する仕組み。iOSはTestFlight、Google Playは内部テスト・クローズドテスト。 |
| Firebase App Distribution | ストアを介さずにテスト用ビルドを配布するサービス。 |
| 署名／署名鍵 | アプリの開発者を証明する処理と、そのための鍵。鍵を失うと更新版を配布できなくなる。 |
| 証明書 | 開発者を証明する資格情報。iOSでは開発用と配布用がある。 |
| プロビジョニングプロファイル | iOSで、どのアプリをどの端末・配布方法で動かしてよいかを定める設定ファイル。 |
| Play App Signing | Googleが署名鍵を預かり、開発者はアップロード鍵で提出する仕組み。 |
| AAB／APK | Androidアプリの提出・配布形式。Google PlayにはAAB（Android App Bundle）で提出し、端末にはAPKが配布される。 |
| IPA | iOSアプリの配布形式。 |
| OTA更新 | ストアの審査を通さずにJavaScript部分を更新する仕組み（React NativeのExpo Updatesなど）。ネイティブ部分は更新できず、ストアの規約にも制約がある。 |
| ASO | App Store Optimization。ストアでの検索やダウンロードを増やすための最適化。 |
| Apple Developer Program／Google Play Console | ストア配布に必要な開発者登録と管理画面。 |

## アプリの仕組み

| 用語 | 説明 |
| :--- | :--- |
| ライフサイクル | 起動、前面、背面、中断、終了といったアプリや画面の状態遷移。OSが制御する。 |
| サンドボックス | アプリごとに隔離された保存領域と実行環境。他のアプリのデータには直接触れない。 |
| 権限（実行時権限） | 位置情報、カメラ、通知などの機能を使うために利用者の許可を得る仕組み。拒否された場合の動作も実装する。 |
| バックグラウンド処理 | アプリが前面にない間に行う処理。OSが実行時間や頻度を制限する。iOSはBackground Tasks、AndroidはWorkManagerが代表的。 |
| Info.plist／AndroidManifest.xml | アプリの設定ファイル。権限、対応OS、起動方法などを記述する。 |
| Activity／Fragment | Androidで画面を構成する部品。Activityは画面全体、Fragmentは画面の一部を担う。 |
| Intent | Androidで画面や機能を呼び出す仕組み。アプリ内の遷移や他アプリとの連携に使う。 |
| ViewController | iOS（UIKit）で画面を管理する部品。 |
| Scene／SceneDelegate | iOSでウィンドウ単位の状態を扱う仕組み。 |
| ディープリンク | URLから特定の画面を直接開く仕組み。iOSのUniversal Links、AndroidのApp Linksは、Webのリンクからアプリを開く。 |
| バックスタック | Androidで画面の履歴を積む仕組み。戻る操作の挙動を決める。 |
| プッシュ通知 | サーバーから端末に通知を送る仕組み。iOSはAPNs、AndroidはFirebase Cloud Messaging（FCM）を経由する。 |

## 言語と並行処理

| 用語 | 説明 |
| :--- | :--- |
| Swift | iOS向けの主要な言語。値型（構造体）と参照型（クラス）、Optionalによる安全な値の扱いが特徴。 |
| Optional | Swiftで「値がないかもしれない」ことを型で表す仕組み。Kotlinの「Null許容型」に相当する。 |
| Objective-C | Swift以前のiOSの言語。古いコードや一部のライブラリで使われる。 |
| Kotlin | Android向けの主要な言語。Null安全、データクラス、拡張関数が特徴。Javaと相互運用できる。 |
| 並行処理 | 通信や重い計算を画面の更新と並行して行うこと。画面の更新は「メインスレッド」で行い、重い処理は別スレッドに逃がす。 |
| メインスレッド（UIスレッド） | 画面の描画と操作の処理を担うスレッド。ここを長時間占有すると画面が固まる。 |
| async／await | 非同期処理を順次処理のように書く構文。SwiftとJavaScriptにある。 |
| コルーチン | Kotlinの非同期処理の仕組み。中断と再開ができる軽量な処理単位。 |
| Flow | Kotlinで値の流れを表す型。StateFlowは現在の状態を保持する。 |
| GCD／DispatchQueue | iOSで処理をキューに入れて実行する仕組み。 |
| actor | Swiftで、共有データへの同時アクセスを防ぐ型。 |
| structured concurrency | 非同期処理の開始と終了を親子関係で管理し、取りこぼしを防ぐ考え方。 |
| ARC／循環参照 | Swiftのメモリ管理方式と、互いに参照し合って解放されない状態。weak参照で防ぐ。 |
| リアクティブプログラミング | 値の変化を購読し、変化に応じて画面や処理を自動的に更新する考え方。iOSのCombine、AndroidのFlowやLiveData、RxSwift／RxJavaが該当する。 |

## UI

| 用語 | 説明 |
| :--- | :--- |
| 宣言的UI | 状態を書き換えると画面が追従する作り方。SwiftUI、Jetpack Compose、React Nativeが該当する。 |
| 命令的UI | 画面の部品を直接操作して更新する作り方。UIKit、Android Views（XML）が該当する。 |
| SwiftUI | Appleの宣言的UIフレームワーク。 |
| UIKit | Appleの命令的UIフレームワーク。既存アプリの多くで使われる。 |
| Jetpack Compose | Androidの宣言的UIフレームワーク。 |
| Composable | Composeで画面の部品を定義する関数。 |
| 再コンポジション | Composeで、状態の変化に応じて部品を再描画する処理。 |
| Storyboard／XIB | UIKitで画面を図として編集するファイル。 |
| Auto Layout／ConstraintLayout | 画面サイズに応じて部品の位置を制約で決める仕組み。iOSとAndroidでそれぞれの名称。 |
| Safe Area | 画面の切り欠きやホームバーと重ならない表示領域。 |
| Dynamic Type／フォントスケール | 利用者が設定した文字サイズに追従する仕組み。iOSとAndroidでそれぞれの名称。 |
| HIG／Material Design | Apple（Human Interface Guidelines）とGoogleのデザイン指針。 |
| VoiceOver／TalkBack | 画面読み上げ機能。iOSとAndroidでそれぞれの名称。 |
| Accessibility Inspector／Accessibility Scanner | アクセシビリティの検査ツール。XcodeとAndroidでそれぞれの名称。 |
| ローカライズ | 言語や地域に合わせて文言、日付、数値の表示を切り替えること。 |

## データと通信

| 用語 | 説明 |
| :--- | :--- |
| UserDefaults／SharedPreferences | 小さな設定値を保存する仕組み。iOSとAndroidでそれぞれの名称。AndroidではDataStoreが後継。 |
| Keychain／Keystore | 秘密情報（パスワード、トークン、鍵）を保護して保存する仕組み。iOSとAndroidでそれぞれの名称。 |
| Core Data／SwiftData／Room | 構造化データをデータベースに保存する仕組み。iOSはCore DataとSwiftData、AndroidはRoom。 |
| SQLite | 端末内で使う軽量なデータベース。各仕組みの基盤にもなっている。 |
| AsyncStorage／expo-secure-store | React Nativeの保存手段。前者は通常のデータ、後者は秘密情報向け。 |
| URLSession／OkHttp／fetch | HTTP通信の基本API。iOS、Android、React Nativeでそれぞれの名称。 |
| Alamofire／Retrofit | 通信を簡潔に書くためのライブラリ。iOSとAndroidでそれぞれの代表例。 |
| Codable／kotlinx.serialization | JSONと型を相互変換する仕組み。SwiftとKotlinでそれぞれの名称。 |
| ATS／Network Security Config | 通信の暗号化と証明書検証に関する設定。iOS（App Transport Security）とAndroidでそれぞれの名称。 |
| 証明書ピンニング | 特定の証明書だけを信頼して通信の改ざんを防ぐ手法。 |
| オフラインファースト | 端末内のデータを正とし、通信できるときにサーバーと同期する設計。 |
| 冪等（べきとう） | 同じ要求を何度送っても結果が変わらない性質。再送しても二重登録が起きないようにする考え方。 |
| Repository | データの取得元（通信、保存）を隠して画面側に一つの窓口を提供する層。 |

## 設計とツール

| 用語 | 説明 |
| :--- | :--- |
| MVVM／MVI／MVC／VIPER／TCA | 画面、状態、データ取得の責務を分けるための設計パターンの名称。チームで一つを選び、責務の境界を揃える。 |
| 依存性注入（DI） | 部品が必要とする相手を外から渡す設計。テスト時に差し替えやすくなる。AndroidのHilt、Koin、SwiftのEnvironmentなどが道具。 |
| Xcode／Android Studio | iOSとAndroidの開発環境。 |
| Expo | React Nativeの環境構築、ビルド、配布を支援する基盤。Managed（Expoが管理）とBare（ネイティブプロジェクトを直接扱う）がある。 |
| Metro | React NativeのJavaScriptバンドラー。 |
| Hermes | React Native向けのJavaScriptエンジン。起動時間とメモリを改善する。 |
| Swift Package Manager／CocoaPods／Gradle | 依存ライブラリの管理とビルドの仕組み。iOSはSwift Package ManagerとCocoaPods、AndroidはGradle。 |
| xcframework | 複数プラットフォーム向けのiOSライブラリの配布形式。 |
| SwiftLint／SwiftFormat／ktlint／detekt | 静的解析と整形のツール。SwiftとKotlinでそれぞれの代表例。 |
| R8／難読化 | Androidでコードを縮小し、名前を読みにくくする処理。クラッシュ解析にはマッピングファイルが必要。 |
| fastlane | ビルド、署名、配布を自動化するツール。 |
| Xcode Cloud／Bitrise／GitHub Actions | CI／CDの実行基盤。iOSのビルドにはmacOSの実行環境が必要。 |

## 品質と運用

| 用語 | 説明 |
| :--- | :--- |
| XCTest／Swift Testing／JUnit／Jest | ユニットテストの枠組み。iOS、Android、React Nativeでそれぞれの名称。 |
| XCUITest／Espresso／Detox／Maestro | UIテストの枠組み。画面操作を自動化して確認する。 |
| Firebase Test Lab | クラウド上の端末でテストを実行するサービス。 |
| Instruments／Android Profiler | 性能とメモリを計測する道具。XcodeとAndroid Studioでそれぞれの名称。 |
| LeakCanary | Androidのメモリリーク検出ライブラリ。 |
| MetricKit／Android vitals | 端末上の性能・安定性データを提供する仕組み。iOSとGoogle Playでそれぞれの名称。 |
| ANR | Application Not Responding。Androidでアプリが一定時間応答しない状態。iOSでは「ハング」と呼ぶ。 |
| クラッシュ率／クラッシュフリー率 | 異常終了したセッションや利用者の割合と、その逆の割合。 |
| Crashlytics | クラッシュを収集・分析するサービス。 |
| シンボル化 | クラッシュ位置を人が読めるソースの位置に対応付ける処理。iOSはdSYM、AndroidはR8のマッピングファイルが必要。 |
| dSYM | iOSのシンボル化に必要な記号ファイル。 |
| Baseline Profile | Androidで起動を速くするための事前コンパイル情報。 |
| 機能フラグ | 機能の有効・無効を配布後に切り替える仕組み。Remote Configなどで実現する。 |
| OWASP MASVS／MASTG | モバイルアプリのセキュリティ検証基準と、そのテスト手順書。 |
| App Tracking Transparency（ATT） | iOSで利用者の追跡許可を求めるダイアログ。 |
| プライバシーマニフェスト／データセーフティ | アプリが扱うデータを申告する仕組み。App StoreとGoogle Playでそれぞれの名称。 |
| SDK | ソフトウェア開発キット。本書では、計測・広告・クラッシュ収集などのために組み込む外部ライブラリを指すことが多い。 |
