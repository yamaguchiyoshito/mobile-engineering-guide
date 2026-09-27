---
title: "モバイルセキュリティ"
description: "モバイルセキュリティの基準と使い方。モバイルアプリ開発の習熟度評価・チーム改善ガイド。"
---

# モバイルセキュリティ

**要素技術ID：** `mobile.security`  
**技術領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** ネットワーク通信、データ永続化

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

## この要素技術について

アプリが扱うパスワード、認証トークン、個人情報などを、端末の中と通信の途中で守る技術です。サーバーのコードと違い、ストアで配布したアプリは第三者が端末に取り込んで中身を解析できるため、APIキーなどの秘密情報をアプリに埋め込んでも隠し通すことはできず、秘密はサーバー側で管理する必要があります。最初に押さえるのは、アプリ側の値や判定は書き換えられ得る前提で重要な検証をサーバーで行うことと、認証情報をKeychainやKeystoreなどOSが用意する保護された保存先に置くことです。

分からない用語は[用語集](../../guide/glossary.md)で確認できます。

## Lv0

端末内の保存領域、通信経路、認証情報、アプリに埋め込んだ値の信頼性の違いを説明できず、安全な実装の確認に手順ごとの指示が必要である。

## Lv1

開発ガイドに沿って、認証情報の保護された保存や暗号化通信の既存の仕組みを利用できる。検査の指摘は支援を受けて確認・修正できる。

## Lv2

機密情報の平文保存、ログへの個人情報出力、アプリへの秘密情報の埋め込み、不要な権限要求などの代表的なリスクを実装箇所と結び付けて説明できる。承認された方式で対策し、配布したアプリは解析され得る前提で、サーバー側の検証と併せて保護を確認できる。

## Lv3

データの流れと信頼境界から脅威を整理し、通信の改ざん、改変された端末、生体認証の扱い、依存ライブラリ、難読化の限界を評価できる。業界の検証基準を参照して許可された環境で問題を再現・修正し、専門担当者に相談すべき範囲を判断できる。

## Lv4

実装基準、保存・通信の共通部品、静的検査と依存関係検査、例外管理、脆弱性対応の手順を関係者と整備できる。チームでの運用実績を基に、指摘の再発と修正までの時間が改善したことを確認できる。

## 次のLvへ進むために

学習の目安として、次の段階に進むための課題と参考資料を示します。課題は評価の条件ではありません。

| 目標 | 取り組む課題の例 | 参考資料 |
| :--- | :--- | :--- |
| Lv1 | 公式ドキュメントに沿って、ログイン後に受け取るトークンをKeychain、Keystore、またはexpo-secure-storeに保存・読み出し・削除するサンプルを作り、通常の設定値と同じ保存先に置かないことを確認する | [Keychain Services](https://developer.apple.com/documentation/security/keychain-services)・[Keystore](https://developer.android.com/privacy-and-security/keystore)・[セキュリティ（React Native）](https://reactnative.dev/docs/security) |
| Lv2 | 自分が作ったアプリを見直し、平文で保存している秘密情報、ログに出力している個人情報、アプリに埋め込んだAPIキー、不要な権限要求を一覧にして修正する。APIキーが必要な処理はサーバー経由の呼び出しに置き換える | [セキュリティのヒント](https://developer.android.com/privacy-and-security/security-tips)・[セキュリティ（React Native）](https://reactnative.dev/docs/security)・[OWASP MAS](https://mas.owasp.org/) |
| Lv3 | OWASP MASVSの項目を参照して既存アプリのデータの流れと信頼境界を図にまとめ、通信の改ざんや改変された端末での動作を許可された検証環境で確かめる。見つかった問題の対策案と、専門担当者に相談すべき範囲を文書にする | [OWASP MAS](https://mas.owasp.org/)・[セキュリティのヒント](https://developer.android.com/privacy-and-security/security-tips) |

## 技術の対応

| 用途 | iOS | Android | React Native |
| :--- | :--- | :--- | :--- |
| 秘密情報の保存 | Keychain、Data Protection | Keystore、EncryptedSharedPreferences／DataStoreの暗号化 | expo-secure-store |
| 通信の保護 | App Transport Security、証明書ピンニング | Network Security Config | ネイティブ層の設定 |
| 解析への備えと秘密情報の扱い | 難読化の限界 | R8による難読化 | 環境変数と秘密情報の扱い、JSバンドルへの秘密情報混入防止 |
| 本人確認・端末確認・権限 | 生体認証（LocalAuthentication） | Play Integrity、実行時権限 | expo-local-authentication |
| 検証基準 | OWASP MASVS／MASTG | OWASP MASVS／MASTG | OWASP MASVS／MASTG |

## 関連ライブラリと参考資料

主な一次情報の所在です。掲載は公式資料と、技術の対応表に挙げた広く使われるライブラリに限ります。採用を推奨するものではありません。

<!-- references:start ids="keychain-services, ios-data-protection, ats, local-authentication, android-keystore, encrypted-shared-preferences, android-network-security-config, android-app-optimization, play-integrity, android-runtime-permissions, expo-securestore, expo-local-authentication, rn-security, owasp-masvs, owasp-mastg" -->

| 種別 | 名称 | 対象 | 概要 |
| :--- | :--- | :--- | :--- |
| 公式リファレンス | [Keychain Services](https://developer.apple.com/documentation/security/keychain-services) | iOS | パスワードやトークンなどの秘密情報を暗号化して保存するAPI |
| 公式リファレンス | [ファイルの暗号化（iOS）](https://developer.apple.com/documentation/uikit/encrypting-your-app-s-files) | iOS | Data Protectionでアプリのファイルを端末上で暗号化する方法 |
| 公式リファレンス | [Preventing Insecure Network Connections](https://developer.apple.com/documentation/security/preventing-insecure-network-connections) | iOS | App Transport Securityで安全でない通信を防ぐ設定の説明 |
| 公式リファレンス | [LocalAuthentication](https://developer.apple.com/documentation/localauthentication) | iOS | 生体認証やパスコードで本人確認を行うフレームワーク |
| 公式リファレンス | [Android Keystore system](https://developer.android.com/privacy-and-security/keystore) | Android | 暗号鍵を端末内の保護された領域で生成し、保管する仕組み |
| 公式リファレンス | [EncryptedSharedPreferences](https://developer.android.com/reference/androidx/security/crypto/EncryptedSharedPreferences) | Android | キーと値を暗号化して保存するSharedPreferencesの実装 |
| 公式リファレンス | [Network security configuration](https://developer.android.com/privacy-and-security/security-config) | Android | 信頼する証明書や平文通信の可否をXMLで宣言する設定 |
| 公式リファレンス | [アプリの最適化（Android）](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) | Android | R8によるコードの縮小と難読化を有効にする方法を説明 |
| 公式リファレンス | [Play Integrity API](https://developer.android.com/google/play/integrity) | Android | アプリと端末が改変されていない正規のものかをサーバーで判定するAPI |
| 公式リファレンス | [実行時の権限リクエスト（Android）](https://developer.android.com/training/permissions/requesting) | Android | 危険な権限を実行時にユーザーへ要求する手順を説明 |
| ライブラリ | [SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/) | React Native | 端末の安全な保存領域にキーと値を暗号化して保存するライブラリ |
| ライブラリ | [expo-local-authentication](https://docs.expo.dev/versions/latest/sdk/local-authentication/) | React Native | FaceIDや指紋などの生体認証を呼び出すExpoのライブラリ |
| 学習資料 | [OWASP MASVS](https://mas.owasp.org/MASVS/) | 共通 | モバイルアプリのセキュリティ要件を分野ごとに定めた検証基準 |
| 学習資料 | [OWASP MASTG](https://mas.owasp.org/MASTG/) | 共通 | モバイルアプリのセキュリティをテスト・解析する手法をまとめたガイド |
| 学習資料 | [セキュリティ（React Native）](https://reactnative.dev/docs/security) | React Native | 秘密情報の保存・通信・認証などReact Nativeアプリの安全対策の解説 |

<!-- references:end -->

## 評価を記録する

[個人の習熟度評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
