---
title: "学習コンテンツ：Android"
description: "学習コンテンツ：Androidの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# 学習コンテンツ：Android

Androidアプリ開発を学ぶ人向けに、34の要素技術のうちAndroidと共通の28件を段階順に並べ、課題と学習資料をまとめたページです。KotlinとJetpack Composeを中心に学び、既存アプリの保守に備えてViewsとFragmentも段階3で扱います。

## このページの使い方

[学習の進め方](../learning-paths.md)の3段階に沿って、要素技術ごとに概要、取り組む課題の例、学習資料をまとめています。課題は各要素技術のページの「次のLvへ進むために」と同じ内容で、評価の条件ではありません。段階の到達目安は、段階1が対象の要素技術でLv1、段階2が主要な要素技術でLv2、段階3が担当領域でLv2〜Lv3です。

同じ課題に取り組んだら、[個人の習熟度評価記録](../../templates/individual-assessment.md)に、作ったもの、確認した結果、支援を受けた範囲を残します。分からない用語は[用語集](../glossary.md)で確認できます。

## 最初に読むもの

- [モバイルアプリ開発の前提](../mobile-basics.md)：Webとの違い、3つのプラットフォーム、必要な開発環境。
- [開発環境（Xcode／Android Studio／Expo）](../../skills/foundation/ide.basic.md)：Android Studioのプロジェクト構成、エミュレータ、Logcatの使い方。
- [用語集](../glossary.md)：Activity、Intent、コルーチン、Keystore、AABなど、Androidの学習で最初に出会う用語。
- roadmap.sh の[Android Developer Roadmap](https://roadmap.sh/android)：学習順序の全体像。

## 公式コースとチュートリアル

プラットフォーム全体を通して学べる公式の教材です。段階1の課題と並行して進めます。

<!-- references:start ids="android-courses, android-basics-compose, compose-tutorial, compose-pathway, kotlin-docs, kotlin-koans, android-codelabs" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 学習資料 | [Android Developers Courses](https://developer.android.com/courses) | Android | Android公式の学習コースとパスウェイの一覧 |
| 学習資料 | [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) | Android | KotlinとComposeでアプリを作りながら学ぶ公式コース |
| 学習資料 | [Jetpack Compose Tutorial](https://developer.android.com/develop/ui/compose/tutorial) | Android | Composeで最初の画面を作る公式チュートリアル |
| 学習資料 | [Jetpack Compose for Android Developers](https://developer.android.com/courses/pathways/compose) | Android | Composeの基礎から状態管理までを学ぶ公式パスウェイ |
| 学習資料 | [Kotlinドキュメント（Android）](https://kotlinlang.org/docs/home.html) | Android | Kotlin言語の入門から応用までをまとめた公式文書 |
| 学習資料 | [Kotlin Koans](https://kotlinlang.org/docs/koans.html) | Android | 演習問題を解きながらKotlinの文法を学ぶ公式教材 |
| 学習資料 | [Android Codelabs](https://developer.android.com/codelabs) | Android | 手順どおりに進めて学ぶ公式の実習教材の一覧 |

<!-- references:end -->

<!-- learning:start -->

## 段階1：最初の1か月

開発環境を整え、言語の基本と画面の作り方を覚え、小さなアプリを動かす。到達目安は対象の要素技術でLv1です。

### モバイルプラットフォーム基礎

スマートフォンのOSの上でアプリがどのように動き、どのような制約を受けるかを理解するための基礎知識です。詳しくは[モバイルプラットフォーム基礎のページ](../../skills/foundation/mobile.basic.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式チュートリアルに沿って新規アプリを作り、起動、背面への移行、前面への復帰のたびにログを出力して、ライフサイクルの各状態で処理が呼ばれる順序を確認する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Activity入門](https://developer.android.com/guide/components/activities/intro-activities)・[はじめに（React Native）](https://reactnative.dev/docs/getting-started) |
| Lv2 | カメラまたは位置情報を使う1画面のアプリを作り、権限を許可した場合と拒否した場合のそれぞれの表示を実装する。入力途中でアプリを背面に移してから戻しても、入力内容が残っていることを端末上で確認する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Activity入門](https://developer.android.com/guide/components/activities/intro-activities)・[Expoドキュメント](https://docs.expo.dev/) |
| Lv3 | 既存のアプリで、背面にある間にプロセスが終了された後の復帰、画面回転などの構成変更、設定画面から権限を取り消した後の起動を再現し、状態が失われる箇所を一覧にして改善案を比べる。ストアの審査基準のうち権限とバックグラウンド実行に関わる項目を読み、設計への影響を整理する | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)・[Background Tasks](https://developer.apple.com/documentation/backgroundtasks)・[バックグラウンド処理](https://developer.android.com/develop/background-work)・[アプリの公開](https://developer.android.com/studio/publish) |

### 開発環境（Xcode／Android Studio／Expo）

アプリのコードを書き、ビルドして端末で動かし、不具合を調べるための開発環境の使い方を扱います。詳しくは[開発環境（Xcode／Android Studio／Expo）のページ](../../skills/foundation/ide.basic.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿って新規プロジェクトを作成し、シミュレータ・エミュレータと実機の両方で起動する。ボタンを押したときの処理にブレークポイントを置き、変数の値とログを確認する | [Xcode](https://developer.apple.com/documentation/xcode)・[Android Studio](https://developer.android.com/studio)・[環境構築（React Native）](https://reactnative.dev/docs/environment-setup) |
| Lv2 | サンプルアプリに画面を1つ追加し、あらかじめ仕込んだ表示崩れや計算の誤りを、ステップ実行、ログ、画面構造の検査機能を使って見つけて修正する | [Xcode](https://developer.apple.com/documentation/xcode)・[Android Studio](https://developer.android.com/studio)・[Expoドキュメント](https://docs.expo.dev/) |
| Lv3 | 実機でのみ起きる不具合（権限、性能、センサーなど）を題材に、シミュレータ・エミュレータとの差を切り分ける調査手順を書き、他の人が同じ手順で再現できるかを確かめる | [アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[Android Studio](https://developer.android.com/studio)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |

### Kotlin

Androidアプリを作るための主要なプログラミング言語であるKotlinの文法と、型の使い方を扱います。詳しくは[Kotlinのページ](../../skills/foundation/kotlin.basic.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Kotlinドキュメントの基本構文の例をAndroid Studioで実行し、関数、ラムダ、データクラスのプロパティを書き換えて結果の変化を確かめる。null許容型の値を ?.と ?: で扱う短い関数を書く | [Kotlinドキュメント](https://kotlinlang.org/docs/home.html)・[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) |
| Lv2 | 買い物リストの合計金額を計算する処理を、データクラス、コレクション操作、拡張関数、sealed classによる結果の分岐で実装し、空のリストや不正な数量を与えたときの振る舞いを単体テストで確認する | [Kotlinドキュメント](https://kotlinlang.org/docs/home.html)・[テスト](https://developer.android.com/training/testing) |
| Lv3 | Javaで書かれたライブラリの戻り値や、複数の箇所で共有している可変コレクションを扱う既存のコードを調べ、nullの混入や意図しない変更が起きる箇所を洗い出す。スコープ関数を重ねた処理を読みやすい形に書き直す案を比べる | [Kotlinドキュメント](https://kotlinlang.org/docs/home.html)・[AndroidのKotlin](https://developer.android.com/kotlin) |

学習資料：[Kotlinドキュメント（Android）](https://kotlinlang.org/docs/home.html)・[AndroidでのKotlin（Android）](https://developer.android.com/kotlin)・[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)

### Jetpack Compose

Jetpack Composeは、Androidアプリの画面をKotlinの関数（Composable）の組み合わせで作るGoogleの仕組みで、画面サイズや文字サイズ、ダークモードなど端末ごとに異なる表示条件にも同じコードで対応します。詳しくは[Jetpack Composeのページ](../../skills/implementation/compose.basic.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Android Basics with Composeのコースに沿って、テキストと画像を並べた画面と、ボタンを押すと数値が増えるカウンターを作り、プレビューとエミュレーターで表示を確認する | [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) |
| Lv2 | 一覧・詳細・追加の3画面を持つToDoアプリを作り、LazyColumnで一覧を表示し、ViewModelの状態を購読してNavigation Composeで遷移する。画面を回転しても入力中の内容が残ることを確認する | [Jetpack Compose](https://developer.android.com/develop/ui/compose)・[Navigation](https://developer.android.com/guide/navigation)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture) |
| Lv3 | 既存の画面で不要な再コンポジションが起きている箇所をAndroid StudioのLayout Inspectorで見つけて減らし、LaunchedEffectの起動条件を見直す。Viewで作られた既存画面にComposableを1つ組み込み、共存の方針をまとめる | [Jetpack Compose](https://developer.android.com/develop/ui/compose)・[パフォーマンス（Android）](https://developer.android.com/topic/performance) |

学習資料：[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)

### UIデザイン原則とローカライズ

アプリの画面を、各OSの見た目と操作の慣習に合わせ、さまざまな画面の大きさや言語でも崩れないように組み立てるための技術です。詳しくは[UIデザイン原則とローカライズのページ](../../skills/applied-foundation/mobile.ui-design.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式チュートリアルに沿ってプロフィール画面を作り、デザインどおりに余白、文字、アイコンを配置する。画面の文字列をリソースに分け、画面の小さい端末と大きい端末のシミュレーターで表示を確認する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)・[スタイル（React Native）](https://reactnative.dev/docs/style) |
| Lv2 | 設定画面を作り、縦横の向き、ダークモード、日本語と英語の切り替えに対応させる。長い訳文、複数形、日付と数値の書式を入れて表示が崩れないことを確認する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Material Design 3](https://m3.material.io/)・[Flexbox（React Native）](https://reactnative.dev/docs/flexbox) |
| Lv3 | スマートフォン向けの既存画面を、タブレットと右から左へ書く言語に対応させる設計を行う。iOSとAndroidで操作の慣習が異なる箇所（戻る操作、タブの位置など）を洗い出し、ブランド表現と両立する案をデザイナーと比較する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Material Design 3](https://m3.material.io/)・[プラットフォーム固有コード（React Native）](https://reactnative.dev/docs/platform-specific-code) |

### Git

ソースコードの変更履歴を記録し、複数人で同じコードを並行して変更して取りまとめるための道具であるGitの使い方を扱います。詳しくは[Gitのページ](../../skills/foundation/git.basic.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 練習用のリポジトリでブランチを作成し、画面の文言を変更して差分を確認してから、ステージング、コミット、pushを行う。ビルドで生成されたファイルがコミットに含まれていないことを確認する | [Pro Git（日本語）](https://git-scm.com/book/ja/v2) |
| Lv2 | 2つのブランチで同じファイルの同じ箇所を変更して競合を起こし、解消後にアプリをビルド・起動して意図した内容になっていることを確認する。同じ作業をmergeとrebaseの両方で行って履歴の違いを比べ、プルリクエストでレビューを依頼する | [Pro Git（日本語）](https://git-scm.com/book/ja/v2)・[GitHub Pull Request](https://docs.github.com/ja/pull-requests) |
| Lv3 | 練習用のリポジトリで、共有ブランチにpushした誤ったコミットをrevertで取り消し、reflogから失われたコミットを復元する。Xcodeのプロジェクトファイルなど競合しやすいファイルの扱いを調べ、チームの手順案をまとめる | [Pro Git（日本語）](https://git-scm.com/book/ja/v2) |

学習資料：[Pro Git（日本語）](https://git-scm.com/book/ja/v2)・[ファイルを無視する（GitHub Docs）](https://docs.github.com/ja/get-started/git-basics/ignoring-files)・[Git Large File Storageについて（GitHub Docs）](https://docs.github.com/ja/repositories/working-with-files/managing-large-files/about-git-large-file-storage)・[プルリクエスト（GitHub Docs）](https://docs.github.com/ja/pull-requests)

## 段階2：基本を固める

通信、保存、画面遷移、テストを含む小さなアプリを自力で完成させる。到達目安は主要な要素技術でLv2です。

### Kotlinコルーチン・Flow

通信やデータベースへのアクセスのように時間のかかる処理を、画面の操作を止めずに実行するためのKotlinの仕組み（コルーチン）と、時間とともに変わる値を流れとして扱う仕組み（Flow）を扱う技術です。詳しくは[Kotlinコルーチン・Flowのページ](../../skills/applied-foundation/kotlin.coroutines.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式コースやガイドの例に沿って、ボタンを押すと数秒待ってから結果を表示するアプリを作り、ログで実行スレッドと処理の完了順序を確認する | [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html) |
| Lv2 | ViewModelからStateFlowで「読み込み中・成功・失敗」の状態を公開し、画面で収集して表示する一覧画面を作る。2つのAPIを並列に呼んで結果をまとめる処理を加え、テスト用ディスパッチャを使ったテストで結果を確認する | [Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[テスト](https://developer.android.com/training/testing) |
| Lv3 | 検索欄の入力をFlowで受け取り、入力が止まってから検索する処理にタイムアウトと再試行を加える。画面が非表示の間は収集を止めることを確認し、既存コードのスコープの使い方を見直してキャンセル漏れを洗い出す | [Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Android vitals](https://developer.android.com/topic/performance/vitals) |

学習資料：[Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines)・[Kotlin flows on Android](https://developer.android.com/kotlin/flow)・[StateFlow and SharedFlow](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow)・[Use Kotlin coroutines with lifecycle-aware components](https://developer.android.com/topic/libraries/architecture/coroutines)・[Best practices for coroutines in Android](https://developer.android.com/kotlin/coroutines/coroutines-best-practices)・[Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test)

### ネットワーク通信

アプリからインターネット上のサーバーに問い合わせてデータを受け取り、画面に表示したり、入力内容を送信したりする技術です。詳しくは[ネットワーク通信のページ](../../skills/applied-foundation/mobile.networking.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公開されているAPIを1つ呼び出し、応答のJSONをデータ型に変換して一覧画面に表示する。送受信した内容をログやデバッグツールで確認する | [Foundation（URLSession）](https://developer.apple.com/documentation/foundation)・[ネットワーク接続（Android）](https://developer.android.com/training/basics/network-ops)・[ネットワーク（React Native）](https://reactnative.dev/docs/network) |
| Lv2 | 一覧と詳細の2画面を持つニュース閲覧アプリを作り、読み込み中の表示、ステータスコードごとのエラー表示、再読み込みを実装する。機内モードや不正な応答を再現して表示を確認し、通信部分をモックに差し替えたテストを書く | [Foundation（URLSession）](https://developer.apple.com/documentation/foundation)・[Retrofit](https://github.com/square/retrofit)・[ネットワーク（React Native）](https://reactnative.dev/docs/network)・[テスト（Android）](https://developer.android.com/training/testing) |
| Lv3 | タイムアウト、再試行、キャンセル、認証情報の付与をまとめた通信層を設計し、低速回線を再現して挙動を確かめる。既存アプリの通信処理を読み、エラー処理の抜けや安全でない通信設定を洗い出す | [OWASP MAS](https://mas.owasp.org/)・[セキュリティのヒント（Android）](https://developer.android.com/privacy-and-security/security-tips)・[セキュリティ（React Native）](https://reactnative.dev/docs/security) |

学習資料：[ネットワーク接続の基本（Android）](https://developer.android.com/training/basics/network-ops)・[Read network state](https://developer.android.com/develop/connectivity/network-ops/reading-network-state)

### データ永続化

アプリが扱うデータを端末の中に保存し、次回起動時や通信できないときにも使えるようにする技術です。詳しくは[データ永続化のページ](../../skills/applied-foundation/mobile.persistence.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 例に沿って、表示テーマの切り替えなど1つの設定値を保存するアプリを作り、アプリを終了して再起動しても値が残ることを確認する | [Foundation（UserDefaults）](https://developer.apple.com/documentation/foundation)・[データストレージ（Android）](https://developer.android.com/training/data-storage)・[Expoドキュメント](https://docs.expo.dev/) |
| Lv2 | 一覧と詳細の2画面を持つメモアプリを作り、メモをデータベースに保存して、アプリを終了しても内容が残ることを確認する。ログイン用のトークンは通常のデータと分けて安全な保存領域に保存する | [SwiftData](https://developer.apple.com/documentation/swiftdata)・[Room](https://developer.android.com/training/data-storage/room)・[Keychain Services](https://developer.apple.com/documentation/security/keychain-services)・[Keystore](https://developer.android.com/privacy-and-security/keystore)・[Expoドキュメント](https://docs.expo.dev/) |
| Lv3 | メモアプリに項目を追加するスキーマ変更を行い、旧バージョンで保存したデータが新バージョンで読めることをテストで確認する。数千件のデータで一覧表示と書き込みの速度を測り、サーバーから取得したデータのキャッシュを更新する方針を決める | [Core Data](https://developer.apple.com/documentation/coredata)・[Room](https://developer.android.com/training/data-storage/room)・[データストレージ（Android）](https://developer.android.com/training/data-storage) |

学習資料：[データストレージ（Android）](https://developer.android.com/training/data-storage)

### 画面遷移とディープリンク

アプリの中で画面を切り替える仕組みと、URLや通知から特定の画面を直接開く仕組み（ディープリンク）を扱う技術です。詳しくは[画面遷移とディープリンクのページ](../../skills/implementation/mobile.navigation.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 一覧から詳細へIDを渡して遷移し、戻る操作で一覧に戻るアプリを公式の手順に沿って作り、iOSのスワイプやAndroidの戻る操作での動作を確認する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Navigation](https://developer.android.com/guide/navigation)・[React Navigation](https://reactnavigation.org/docs/getting-started) |
| Lv2 | 一覧と設定の2つのタブ、一覧から開く詳細、追加用のモーダルを持つアプリを作る。`myapp://items/123`のようなURLで詳細画面を開く処理を加え、アプリが起動していない状態と起動中の状態の両方で確認する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Navigation](https://developer.android.com/guide/navigation)・[React Navigation](https://reactnavigation.org/docs/getting-started) |
| Lv3 | ログインが必要な画面へのリンクを未ログインで開いたとき、ログイン後に元の画面へ進む流れを設計して実装する。ボタンの連打による二重遷移や、OSによるアプリ終了後に復元したときの画面状態を検証する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Navigation](https://developer.android.com/guide/navigation)・[React Navigation](https://reactnavigation.org/docs/getting-started) |

### 入力とバリデーション

文字や数値を入力する欄、画面に表示されるキーボード、入力値の検査と誤りの伝え方をまとめて扱う技術です。詳しくは[入力とバリデーションのページ](../../skills/implementation/mobile.input-validation.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 名前とメールアドレスの2項目を持つ入力画面を作り、メールアドレス用のキーボードを指定して、空欄のまま送信したときにエラーを表示する | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)・[コアコンポーネント](https://reactnative.dev/docs/intro-react-native-components) |
| Lv2 | 5項目程度の会員登録画面を作り、次の項目へのフォーカス移動、キーボードで隠れない配置、項目ごとの検証、送信中の表示と二重送信の防止を実装する。画面の小さい端末と大きい端末の両方で確認する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Jetpack Compose](https://developer.android.com/develop/ui/compose)・[コアコンポーネント](https://reactnative.dev/docs/intro-react-native-components)・[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) |
| Lv3 | 電話番号を入力中に自動で区切る処理と、3段階に分かれた入力画面で途中の内容を保持して前の段階に戻れる仕組みを作る。読み上げ機能（VoiceOver／TalkBack）と外部キーボードで操作できることを確認する | [Accessibility](https://developer.apple.com/documentation/accessibility)・[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[アクセシビリティ（React Native）](https://reactnative.dev/docs/accessibility) |

### ビルドと依存管理

書いたコードと外部のライブラリを組み合わせ、端末にインストールできる形（成果物）にまとめる仕組みを扱います。詳しくは[ビルドと依存管理のページ](../../skills/foundation/build.tooling.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿って、画像の読み込みやHTTP通信などに使う外部ライブラリを1つ追加し、アプリから呼び出してビルド・実行する。開発用の構成で成果物を生成し、その保存場所を確認する | [Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages)・[Gradleビルド](https://developer.android.com/build)・[Expoドキュメント](https://docs.expo.dev/) |
| Lv2 | 開発用とリリース用でAPIの接続先とアプリの表示名が切り替わるようにビルド構成を分け、両方の成果物を生成して、実際に切り替わっていることを確認する。依存ライブラリを1つ更新し、ビルドと動作に問題がないことを確かめる | [Xcode](https://developer.apple.com/documentation/xcode)・[Gradleビルド](https://developer.android.com/build)・[Expo EAS](https://docs.expo.dev/eas/) |
| Lv3 | 既存プロジェクトの依存関係を一覧にし、同じライブラリの異なるバージョンが間接的に入り込んでいる箇所や、ビルド時間の多くを占める工程を調べる。ライブラリを使い続ける案と置き換える案を、保守性、ビルド時間、成果物サイズの観点で比べる | [Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages)・[Gradleビルド](https://developer.android.com/build)・[Expo EAS](https://docs.expo.dev/eas/) |

### ユニットテスト

関数やクラスなどプログラムの小さな部品が仕様どおりに動くかを、コードで自動的に確かめる技術です。詳しくは[ユニットテストのページ](../../skills/quality/test.unit.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントの手順に沿ってテスト用のターゲットやフォルダを用意し、税込み価格を計算する関数などの正常系テストを3件書いて、開発環境とコマンドの両方で実行する | [XCTest](https://developer.apple.com/documentation/xctest)・[Swift Testing](https://developer.apple.com/documentation/testing)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv2 | 通信で取得した一覧を並べ替えて表示用に変換する処理を作り、API呼び出しをテストダブルに置き換えて、非同期処理の完了を待って検証する形で、空の一覧・通信エラー・境界値のテストを書く。実装をわざと壊し、テストが失敗することも確認する | [Swift Testing](https://developer.apple.com/documentation/testing)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv3 | 現在時刻やシングルトンに直接依存している既存コードを選び、依存を外から渡せる形に分けてテストを追加する。実行順や時刻で結果が変わる既存テストを探して原因を説明し、検出力を落とさずに修正する | [依存性注入](https://developer.android.com/training/dependency-injection)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |

学習資料：[Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test)

### チーム開発

複数の開発者が同じアプリのコードを変更するときに、変更内容を提案し、他の人に確認（レビュー）してもらってから本流に取り込むという、チームでの進め方を扱う技術です。詳しくは[チーム開発のページ](../../skills/applied-foundation/git.collaboration.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 練習用のリポジトリでブランチを作って小さな変更を加え、テンプレートに沿って変更理由と確認結果を書いたPRを作成する。レビューの指摘を反映し、CIの結果を確認してからマージする | [Pro Git（日本語）](https://git-scm.com/book/ja/v2)・[GitHub Pull Request](https://docs.github.com/ja/pull-requests) |
| Lv2 | 画面の追加など1つの機能を、レビューしやすい大きさの複数のPRに分けて提出し、セルフレビューとCIの確認を済ませてからレビューを依頼する。あわせて、他のメンバーのPRを目的・影響・確認結果の観点でレビューする | [GitHub Pull Request](https://docs.github.com/ja/pull-requests)・[GitHub Actions](https://docs.github.com/ja/actions) |
| Lv3 | 複数人が並行して進める機能について、ブランチの分け方と取り込む順序を決め、競合の解消を調整する。直近のPRのレビュー待ち時間や差し戻しの理由を集計し、運用の改善案を出す | [Pro Git（日本語）](https://git-scm.com/book/ja/v2)・[GitHub Pull Request](https://docs.github.com/ja/pull-requests)・[GitHub Actions](https://docs.github.com/ja/actions) |

学習資料：[Pro Git（日本語）](https://git-scm.com/book/ja/v2)・[プルリクエスト（GitHub Docs）](https://docs.github.com/ja/pull-requests)

## 段階3：実務で広げる

既存アプリの保守、性能・セキュリティ・配布・監視を担当し、設計判断に関わる。到達目安は担当領域でLv2〜Lv3です。

### Android Views・Fragment

Androidアプリの画面を、XMLで書いたレイアウトと、画面単位の入れ物であるActivityとFragmentで組み立てる技術で、既存のアプリの多くがこの方式で作られています。詳しくは[Android Views・Fragmentのページ](../../skills/implementation/android.views.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | Activity 1つにボタンとテキストを置き、ViewBindingで参照してクリックで表示を変える。別のActivityをIntentで起動し、エミュレーターで動作を確認する | [Activity入門](https://developer.android.com/guide/components/activities/intro-activities)・[Android Studio](https://developer.android.com/studio) |
| Lv2 | RecyclerViewの一覧と詳細の2つのFragmentを持つメモアプリをNavigation Componentで作り、ConstraintLayoutで配置する。画面を回転しても表示と入力内容が保たれることを確認する | [Fragment](https://developer.android.com/guide/fragments)・[Navigation](https://developer.android.com/guide/navigation)・[Material Design 3](https://m3.material.io/) |
| Lv3 | 既存のFragmentで、Viewが破棄された後も参照を持ち続けてリークしている箇所を見つけて直す。一覧全体を更新しているAdapterをDiffUtilによる差分更新に置き換え、表示の変化と処理量を比べる | [Fragment](https://developer.android.com/guide/fragments)・[パフォーマンス（Android）](https://developer.android.com/topic/performance) |

学習資料：[Bottom sheets](https://m3.material.io/components/bottom-sheets/overview)・[Navigation drawer](https://m3.material.io/components/navigation-drawer/overview)

### リアクティブプログラミング

値が変わったときに知らせを受け取り、その知らせをきっかけに画面などを自動で更新する書き方（リアクティブプログラミング）を扱う技術です。詳しくは[リアクティブプログラミングのページ](../../skills/applied-foundation/reactive.basic.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | テキスト入力欄の内容を購読し、入力された文字数を画面に表示するサンプルを作る。画面を閉じるときに購読を解除し、値が届く順序と、解除後に値が届かないことをログで確認する | [Combine](https://developer.apple.com/documentation/combine)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html) |
| Lv2 | 検索欄の入力を購読し、入力が一定時間止まってから検索して結果を一覧に表示する機能を作る。通信エラー時の表示と、画面を閉じたときの購読の解除を実装し、値が発行される順序をテストで確認する | [Combine](https://developer.apple.com/documentation/combine)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html)・[アプリアーキテクチャガイド](https://developer.android.com/topic/architecture) |
| Lv3 | ログイン状態、通信状態、設定値など複数のデータ源を組み合わせて1つの画面の状態を作る流れを設計する。既存コードの購読箇所を洗い出して多重購読や解除漏れを調べ、同じ処理を非同期関数で書いた場合と比較する | [Combine](https://developer.apple.com/documentation/combine)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[Kotlinコルーチンガイド](https://kotlinlang.org/docs/coroutines-guide.html) |

学習資料：[Kotlin flows on Android](https://developer.android.com/kotlin/flow)

### アプリアーキテクチャと依存性注入

アプリのコードを、画面の表示、画面の状態、データの取得や保存といった役割ごとに分け、部品同士のつながり方を決める技術です。詳しくは[アプリアーキテクチャと依存性注入のページ](../../skills/implementation/mobile.architecture.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式のアーキテクチャガイドやチームの既存アプリを読み、画面・状態・データの各役割がどのファイルにあるかを図に書き出す。そのうえで、指定された層に表示項目を1つ追加する | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture) |
| Lv2 | 一覧と詳細の2画面を持つアプリを、表示・状態・データ取得の3層に分けて作る。データ取得の部品を外から渡せるようにし、偽のデータを渡して状態の層のユニットテストを書く | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[依存性注入](https://developer.android.com/training/dependency-injection)・[XCTest](https://developer.apple.com/documentation/xctest)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv3 | 既存アプリの依存関係を図にして、層の越境や循環依存を見つけ、1か所を段階的に直す。画面数やチームの人数を想定して2つ以上のパターンを比較し、選択の理由を文書にまとめる | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages) |

学習資料：[アプリアーキテクチャガイド（Android）](https://developer.android.com/topic/architecture)・[UI layer](https://developer.android.com/topic/architecture/ui-layer)・[Data layer](https://developer.android.com/topic/architecture/data-layer)・[Domain layer](https://developer.android.com/topic/architecture/domain-layer)・[依存性注入（Android）](https://developer.android.com/training/dependency-injection)・[Guide to Android app modularization](https://developer.android.com/topic/modularization)

### API連携とデータフロー

サーバーのAPIから受け取ったデータを、端末内の保存領域と組み合わせて画面に届けるまでの流れを設計・実装する技術です。詳しくは[API連携とデータフローのページ](../../skills/implementation/mobile.api-integration.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公開されているAPIからデータを取得して一覧に表示するアプリを公式の手順に沿って作り、機内モードにして通信に失敗したときの表示を確認する | [Foundation](https://developer.apple.com/documentation/foundation)・[ネットワーク接続](https://developer.android.com/training/basics/network-ops)・[ネットワーク（React Native）](https://reactnative.dev/docs/network) |
| Lv2 | APIから取得した一覧を端末に保存し、次回起動時や通信できないときは保存済みのデータを表示するアプリを作る。読み込み中・空・失敗の表示と、認証トークンの安全な保存を実装する | [Keychain Services](https://developer.apple.com/documentation/security/keychain-services)・[Room](https://developer.android.com/training/data-storage/room)・[Retrofit](https://github.com/square/retrofit)・[セキュリティ（React Native）](https://reactnative.dev/docs/security) |
| Lv3 | 複数の通信が同時に認証切れになったとき、トークンの更新を1回だけ行って元の通信をやり直す仕組みを設計する。再試行の間隔を段階的に延ばす処理とページ分割の読み込みを加え、通信を遅くした環境で検証する | [アプリアーキテクチャガイド](https://developer.android.com/topic/architecture)・[Swift Concurrency](https://developer.apple.com/documentation/swift/concurrency)・[OWASP MAS](https://mas.owasp.org/) |

学習資料：[Data layer](https://developer.android.com/topic/architecture/data-layer)

### アクセシビリティ

目が見えにくい、指先を細かく動かしにくい、色の区別がつきにくいといった、さまざまな利用者がアプリを使えるようにするための設計と実装を扱う技術です。詳しくは[アクセシビリティのページ](../../skills/applied-foundation/mobile.accessibility.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 自分のアプリの1画面で読み上げ機能（VoiceOverまたはTalkBack）を有効にして操作し、ラベルのないボタンや読み上げ順序のおかしい箇所を記録して、支援を受けながら修正する | [Accessibility（Apple）](https://developer.apple.com/documentation/accessibility)・[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[アクセシビリティ（React Native）](https://reactnative.dev/docs/accessibility) |
| Lv2 | ログイン画面を作り、すべての入力欄とボタンにラベルと役割を付け、入力エラーを読み上げで伝える。文字サイズを最大にした状態と検査ツールで確認し、タッチ領域の不足を修正する | [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)・[Material Design 3](https://m3.material.io/)・[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[アクセシビリティ（React Native）](https://reactnative.dev/docs/accessibility) |
| Lv3 | スワイプで削除する一覧や独自のスライダーなど、標準部品にない操作を読み上げ機能でも使えるようにする。モーダルを開いたときのフォーカス移動と、動きを減らす設定への対応を設計し、代替の操作手段を比較する | [Accessibility（Apple）](https://developer.apple.com/documentation/accessibility)・[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[アクセシビリティ（React Native）](https://reactnative.dev/docs/accessibility) |

学習資料：[アクセシビリティ（Android）](https://developer.android.com/guide/topics/ui/accessibility)・[Make apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps)・[Test your app's accessibility](https://developer.android.com/guide/topics/ui/accessibility/testing)

### プラットフォーム機能連携

通知、位置情報、カメラ、地図、バックグラウンドでの処理、アプリ内課金など、OSや端末が提供する機能をアプリから使う技術です。詳しくは[プラットフォーム機能連携のページ](../../skills/implementation/mobile.platform-services.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 手順書に沿って通知の権限を要求し、ボタンを押すと数秒後にローカル通知が届くアプリを作る。実機で権限を許可した場合と拒否した場合の両方を確認する | [User Notifications](https://developer.apple.com/documentation/usernotifications)・[Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) |
| Lv2 | プッシュ通知を受け取り、通知をタップすると関連する画面を開くアプリを作る。定期的なデータ更新をバックグラウンド処理として登録し、権限を拒否・取り消したときの表示も実装して実機で確認する | [User Notifications](https://developer.apple.com/documentation/usernotifications)・[Background Tasks](https://developer.apple.com/documentation/backgroundtasks)・[Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)・[バックグラウンド処理](https://developer.android.com/develop/background-work)・[Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) |
| Lv3 | 既存アプリのバックグラウンド処理と位置情報の利用を洗い出し、OSごとの実行制限と電池消費を踏まえて代替手段を比較する。ストアの審査ガイドラインの該当項目を確認し、権限を求める理由の説明文を見直す | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)・[Background Tasks](https://developer.apple.com/documentation/backgroundtasks)・[バックグラウンド処理](https://developer.android.com/develop/background-work)・[Android vitals](https://developer.android.com/topic/performance/vitals) |

### アニメーションとインタラクション

表示の切り替えや位置・大きさの変化に動きを付け、タップやスワイプなど指の操作に画面を反応させる技術です。詳しくは[アニメーションとインタラクションのページ](../../skills/implementation/mobile.animation.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | ボタンを押すと画像が表示・非表示になり、その際に透明度と位置が変わるアニメーションを公式の例に沿って付ける | [SwiftUIチュートリアル](https://developer.apple.com/tutorials/swiftui)・[Composeのアニメーション](https://developer.android.com/develop/ui/compose/animation/introduction)・[アニメーション（React Native）](https://reactnative.dev/docs/animations) |
| Lv2 | カードを左右にスワイプすると削除でき、途中で指を離すと元の位置に戻る一覧を作る。OSの動きを減らす設定をオンにしたときに動きを控えることを実機で確認する | [SwiftUI](https://developer.apple.com/documentation/swiftui)・[Composeのアニメーション](https://developer.android.com/develop/ui/compose/animation/introduction)・[アニメーション（React Native）](https://reactnative.dev/docs/animations)・[Accessibility](https://developer.apple.com/documentation/accessibility) |
| Lv3 | 動きがかくつく既存画面の描画時間を計測して原因を特定し、描画の負荷が少ない方法に置き換える。スワイプ中にアニメーションが中断されたときに画面の状態が食い違わないことを確認する | [Core Animation](https://developer.apple.com/documentation/quartzcore)・[アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[Viewのアニメーション](https://developer.android.com/develop/ui/views/animations)・[パフォーマンス（Android）](https://developer.android.com/topic/performance)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |

### テスト設計

アプリの要求や仕様を読み、何を、どの条件で、どのように確かめるかを決める技術です。詳しくは[テスト設計のページ](../../skills/quality/test.design.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 既存アプリのログイン画面について、用意された観点表に沿って前提条件・入力・操作・期待結果を持つテストケースを10件程度書き、シミュレータ・エミュレータまたは実機で手順どおりに実行して結果を記録する | [テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv2 | 文字数制限と必須項目がある会員登録画面の仕様から、正常系・異常系・境界値・画面の状態遷移を整理したケース表を作り、各ケースを単体テスト・UIテスト・手動確認のどれで検証するかを割り当てる。仕様から判断できない点は質問事項として分けて書き出す | [XCTest](https://developer.apple.com/documentation/xctest)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv3 | 既存アプリの1機能について、権限の拒否、通信の切断、データの不整合、OSバージョンと画面サイズの違いを含むリスクを洗い出し、既存ケースの不足と重複をレビューする。優先順位と実行する端末の組み合わせを決め、未検証の範囲と残るリスクを文書にまとめる | [Xcode](https://developer.apple.com/documentation/xcode)・[テスト（Android）](https://developer.android.com/training/testing)・[Firebase Test Lab](https://firebase.google.com/docs/test-lab) |

学習資料：[テスト（Android）](https://developer.android.com/training/testing)・[テストの基本（Android）](https://developer.android.com/training/testing/fundamentals)

### UIテスト・E2E

ボタンを押す、文字を入力するといった利用者の操作をプログラムで再現し、画面の表示や一連の流れが期待どおりかを自動で確かめる技術です。詳しくは[UIテスト・E2Eのページ](../../skills/quality/test.ui.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントの手順に沿って、ログイン画面でIDとパスワードを入力してボタンを押し、次の画面の見出しが表示されることを確かめるUIテストを1件作り、シミュレータ・エミュレータで実行する | [XCTest](https://developer.apple.com/documentation/xctest)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview) |
| Lv2 | 一覧・詳細・編集の3画面を持つメモアプリで、「メモを作成すると一覧に表示される」「編集内容が詳細画面に反映される」などの主要シナリオを識別子と待機を使って自動化する。テストごとにデータを初期化し、CIで実行して失敗時の画面記録とログを確認する | [XCTest](https://developer.apple.com/documentation/xctest)・[テスト（Android）](https://developer.android.com/training/testing)・[テストの概要（React Native）](https://reactnative.dev/docs/testing-overview)・[GitHub Actions](https://docs.github.com/ja/actions) |
| Lv3 | 既存アプリのUIテストに、権限ダイアログ、ディープリンクからの起動、通信の切断、バックグラウンドからの復帰を含むシナリオを追加する。複数の端末・画面サイズで並列実行し、不安定なテストの原因をアプリ・テスト・データ・端末環境に分類して改善する | [Firebase Test Lab](https://firebase.google.com/docs/test-lab)・[テスト（Android）](https://developer.android.com/training/testing)・[XCTest](https://developer.apple.com/documentation/xctest) |

### 性能・メモリ・起動時間

アプリが速く起動し、操作に遅れなく反応し、画面が滑らかに動き、メモリや電池を使いすぎないようにする技術です。詳しくは[性能・メモリ・起動時間のページ](../../skills/quality/mobile.performance.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントの手順に沿って、自分のアプリの起動時間とメモリ使用量をプロファイラで計測して記録する。画像を縮小して読み込むなどの改善を1つ適用し、同じ端末・同じ条件で再計測する | [アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[パフォーマンス（Android）](https://developer.android.com/topic/performance)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |
| Lv2 | 画像付きの項目を数百件表示する一覧画面を作り、スクロール中のフレーム落ちとメモリ使用量をリリース相当のビルドで計測する。画像の読み込みと表示部品の再利用を改善し、改善前後の数値と他の画面への影響を記録する | [アプリ性能の改善](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)・[パフォーマンス（Android）](https://developer.android.com/topic/performance)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |
| Lv3 | 既存アプリの起動処理を分析し、初期化の遅延、事前コンパイル、キャッシュなどの改善案をメモリや電池消費への影響と合わせて比較する。性能の異なる端末とデータ量で計測し、実利用データと開発環境での計測結果の違いを説明する | [MetricKit](https://developer.apple.com/documentation/metrickit)・[Android vitals](https://developer.android.com/topic/performance/vitals)・[パフォーマンス（React Native）](https://reactnative.dev/docs/performance) |

### モバイルセキュリティ

アプリが扱うパスワード、認証トークン、個人情報などを、端末の中と通信の途中で守る技術です。詳しくは[モバイルセキュリティのページ](../../skills/quality/mobile.security.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントに沿って、ログイン後に受け取るトークンをKeychain、Keystore、またはexpo-secure-storeに保存・読み出し・削除するサンプルを作り、通常の設定値と同じ保存先に置かないことを確認する | [Keychain Services](https://developer.apple.com/documentation/security/keychain-services)・[Keystore](https://developer.android.com/privacy-and-security/keystore)・[セキュリティ（React Native）](https://reactnative.dev/docs/security) |
| Lv2 | 自分が作ったアプリを見直し、平文で保存している秘密情報、ログに出力している個人情報、アプリに埋め込んだAPIキー、不要な権限要求を一覧にして修正する。APIキーが必要な処理はサーバー経由の呼び出しに置き換える | [セキュリティのヒント](https://developer.android.com/privacy-and-security/security-tips)・[セキュリティ（React Native）](https://reactnative.dev/docs/security)・[OWASP MAS](https://mas.owasp.org/) |
| Lv3 | OWASP MASVSの項目を参照して既存アプリのデータの流れと信頼境界を図にまとめ、通信の改ざんや改変された端末での動作を許可された検証環境で確かめる。見つかった問題の対策案と、専門担当者に相談すべき範囲を文書にする | [OWASP MAS](https://mas.owasp.org/)・[セキュリティのヒント](https://developer.android.com/privacy-and-security/security-tips) |

学習資料：[OWASP MASVS](https://mas.owasp.org/MASVS/)・[OWASP MASTG](https://mas.owasp.org/MASTG/)

### 署名・配布・ストア公開

作ったアプリを利用者の端末に届けるために、署名、テスト配信、ストアへの提出と審査、公開までを行う技術です。詳しくは[署名・配布・ストア公開のページ](../../skills/quality/mobile.release.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿って自分のアプリの配布用ビルドを作成し、TestFlightまたはGoogle Playの内部テストにアップロードして、自分の端末にインストールできることを確認する | [TestFlight](https://developer.apple.com/testflight/)・[アプリの公開](https://developer.android.com/studio/publish)・[Expo EAS](https://docs.expo.dev/eas/) |
| Lv2 | 小さなアプリについて、バージョン番号とビルド番号の更新、署名設定、スクリーンショットと説明文、プライバシーに関する申告を準備し、審査ガイドラインとの適合を確認したうえでストアへの提出から公開まで完了する | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)・[App Store Connectヘルプ](https://developer.apple.com/help/app-store-connect/)・[アプリの公開](https://developer.android.com/studio/publish)・[アプリ署名](https://developer.android.com/studio/publish/app-signing)・[App Storeへの公開](https://reactnative.dev/docs/publishing-to-app-store)・[署名付きAPK](https://reactnative.dev/docs/signed-apk-android) |
| Lv3 | 既存アプリの次回リリースについて、段階的公開の割合と期間、テスト対象者の区分、旧版とAPIの互換性、強制更新の条件、公開後に不具合が見つかった場合の配信停止の手順を含むリリース計画を作り、関係者に説明する | [App Store Connectヘルプ](https://developer.apple.com/help/app-store-connect/)・[アプリの公開](https://developer.android.com/studio/publish)・[Expo EAS](https://docs.expo.dev/eas/) |

### CI/CD・静的解析

コードの変更をリポジトリに送るたびに、ビルド、テスト、コードの書き方の自動検査（静的解析）、テスト配信などを自動で実行する仕組みを作り、運用する技術です。詳しくは[CI/CD・静的解析のページ](../../skills/quality/mobile.cicd.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントに沿って、プッシュのたびに自分のアプリのビルドと単体テストを実行するワークフローを作る。テストをわざと失敗させ、ログから該当箇所を見つける | [GitHub Actions](https://docs.github.com/ja/actions)・[Pro Git（日本語）](https://git-scm.com/book/ja/v2) |
| Lv2 | 小さなアプリのリポジトリに、プルリクエストごとにビルド、静的解析（SwiftLint、ktlint、ESLintなど）、書式検査、単体テストを実行するワークフローを構成する。依存関係のキャッシュを設定し、設定前後の実行時間を比べる | [GitHub Actions](https://docs.github.com/ja/actions)・[GitHub Pull Request](https://docs.github.com/ja/pull-requests)・[Gradleビルド](https://developer.android.com/build) |
| Lv3 | 既存のパイプラインに、署名情報を安全に受け渡して配布用ビルドを作成し、テスト配信まで行う段階を追加する。ジョブの実行時間と不安定な失敗を集計し、段階の分割や並列化で待ち時間を短くする | [fastlane](https://docs.fastlane.tools/)・[Xcode Cloud](https://developer.apple.com/xcode-cloud/)・[Expo EAS](https://docs.expo.dev/eas/)・[GitHub Actions](https://docs.github.com/ja/actions) |

### 監視・クラッシュ分析

公開したアプリで起きたクラッシュ（異常終了）、応答停止、エラーを利用者の端末から集めて分析し、原因の特定と修正につなげる技術です。詳しくは[監視・クラッシュ分析のページ](../../skills/quality/mobile.observability.md)を参照してください。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式の手順に沿ってサンプルアプリにクラッシュ報告の収集を組み込み、テスト用のクラッシュを発生させて、管理画面でスタックトレース、アプリのバージョン、端末を確認して記録する | [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics) |
| Lv2 | 自分のアプリの配布用ビルドでdSYM、ProGuard mapping、ソースマップなどのシンボル情報のアップロードを設定し、読める形になったスタックトレースから原因を特定して修正する。あわせて、個人情報を含めないログの出力規則を決めてアプリに適用する | [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics)・[OSLog](https://developer.apple.com/documentation/os/logging) |
| Lv3 | 既存アプリのクラッシュ率と応答停止をバージョン、端末、OSごとに集計し、影響の大きい順に対応の優先順位を決める。アプリ側の例外とサーバー側の障害を切り分ける手順と、遠隔設定で問題のある機能を止める方法を設計する | [MetricKit](https://developer.apple.com/documentation/metrickit)・[Android vitals](https://developer.android.com/topic/performance/vitals)・[Firebase Crashlytics](https://firebase.google.com/docs/crashlytics) |

<!-- learning:end -->

## 学習の記録

段階ごとに[個人の習熟度評価記録](../../templates/individual-assessment.md)へ、取り組んだ課題、確認した結果、支援を受けた範囲を残します。[記入例：Swiftを学び始めた担当者の個人評価](../../examples/individual-swift-lv1.md)に、学習初期の記録の書き方を示しています。評価の手順は[個人の習熟度を評価する](../individual-assessment.md)を参照してください。
