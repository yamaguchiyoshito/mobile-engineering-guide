---
title: "モバイルセキュリティ"
description: "モバイルセキュリティの基準と使い方。モバイルアプリ開発のスキル評価・チーム改善ガイド。"
---

# モバイルセキュリティ

**スキルID：** `mobile.security`  
**スキル領域：** [品質・高度化領域](index.md)  
**対象プラットフォーム：** 共通  
**主な前提：** ネットワーク通信、データ永続化

[習熟度の共通定義と判定方法](../../guide/individual-assessment.md)に沿って、根拠を確認します。

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

## 技術の対応

| プラットフォーム | 主な技術・API |
| :--- | :--- |
| iOS | Keychain、App Transport Security、証明書ピンニング、Data Protection、生体認証（LocalAuthentication）、難読化の限界、OWASP MASVS／MASTG |
| Android | Keystore、EncryptedSharedPreferences／DataStore の暗号化、Network Security Config、R8 による難読化、Play Integrity、実行時権限、OWASP MASVS／MASTG |
| React Native | expo-secure-store、環境変数と秘密情報の扱い、JS バンドルへの秘密情報混入防止、ネイティブ層の設定 |

roadmap.sh の参照トピック：ios: keychain / android: security, authentication, shared-preferences / swift-ui: access-control / react-native: security, expo-secure-store, authentication

## 評価を記録する

[個人のスキル評価書式](../../templates/individual-assessment.md)に、現在の判定、根拠、支援と制約、次の到達条件を記録します。
