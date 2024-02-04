from datetime import datetime, timedelta

n = int(input())
u = [list(input().split()) for _ in range(n)]
m = int(input())
q = [list(input().split()) for _ in range(m)]

Articles = {}  # 記事データ管理用辞書
"""
key: ArticleID
- "Datetime" : Datetimeオブジェクト
- "UserID": 記事を投稿したユーザーのID
- "Title": 記事のタイトル
- "CommentIDs": コメントIDを保持する配列
- "Views": 閲覧履歴（Datetimeで管理）
- "IsActive": 記事が現在アクティブかどうかを示すbool
"""

Comments = {}  # コメントデータ管理用辞書
"""
key: CommentID
- "Datetime" : Datetimeオブジェクト
- "UserID": コメントを投稿したユーザーのID
- "ArticleID": 記事のID
- "Context": コメント本文
- "IsActive": True,  # コメントが現在アクティブかどうかを示すbool
"""

Users = {}
for user, permission in u:
    Users[user] = {
        "view_history": [],
        "comment": [],
        "permission": True if permission == "1" else False,
    }  # ユーザーデータ管理用辞書
"""
key: UserID
- "view_history": 閲覧した記事IDを保持する配列 (ID, 時刻)
- "comment": コメントIDの履歴を保持する配列
- "permission": ユーザーの権限を示すbool
"""

for act, *query in q:

    # ニュース記事投稿クエリ
    if act == "post_article:":

        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[0] + " " + query[1], "%Y-%m-%d %H:%M:%S")
        UserID, ArticleID, Title = query[2], query[3], query[4]

        # ユーザーが権限を有しているかのチェック
        if not Users[UserID]["permission"]:
            print("post_article: unauthorized")

        # 記事がすでに投稿されているかの確認
        elif ArticleID in Articles.keys():
            print("post_article: duplicated")

        # 記事投稿
        else:
            # 辞書に追加
            Articles[ArticleID] = {
                "Datetime": Datetime,
                "UserID": UserID,
                "Title": Title,
                "CommentIDs": [],  # コメントのIDリスト
                "Views": [],  # 閲覧履歴（Datetimeで管理）
                "IsActive": True,  # 記事の存在フラグ
            }

            print(f"post_article: {ArticleID} {Title}")

    # ニュース記事削除クエリ
    elif act == "delete_article:":

        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[0] + " " + query[1], "%Y-%m-%d %H:%M:%S")
        UserID, ArticleID = query[2], query[3]

        # 記事の存在をIDでチェック (未投稿or削除済み)
        if ArticleID not in Articles.keys() or (
            ArticleID in Articles.keys() and not Articles[ArticleID]["IsActive"]
        ):
            print("delete_article: not found")

        # ユーザーIDが記事の投稿者と一致するかチェック
        elif UserID != Articles[ArticleID]["UserID"]:
            print("delete_article: unauthorized")

        # 記事削除
        else:
            # 有効コメント数を取得
            comments_count = sum(
                1
                for CommentID in Articles[ArticleID]["CommentIDs"]
                if Comments[CommentID]["IsActive"]
            )

            # 記事内コメントも削除
            for CommentID in Articles[ArticleID]["CommentIDs"]:
                Comments[CommentID]["IsActive"] = False

            print(f"delete_article: {ArticleID} {comments_count}")
            Articles[ArticleID]["IsActive"] = False  # 記事の存在フラグを無効化

    # ニュース記事閲覧クエリ
    elif act == "view_article:":

        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[0] + " " + query[1], "%Y-%m-%d %H:%M:%S")
        UserID, ArticleID = query[2], query[3]

        # 記事の存在をIDでチェック (未投稿or削除済み)
        if ArticleID not in Articles.keys() or (
            ArticleID in Articles.keys() and not Articles[ArticleID]["IsActive"]
        ):
            print("view_article: not found")

        # 記事閲覧
        else:
            print(f"view_article: {UserID} {ArticleID}")

            # 閲覧履歴追加
            Users[UserID]["view_history"].append((Datetime, ArticleID))
            Articles[ArticleID]["Views"].append(Datetime)

    # コメント投稿クエリ
    if act == "post_comment:":

        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[0] + " " + query[1], "%Y-%m-%d %H:%M:%S")
        UserID, ArticleID, CommentID, Context = query[2], query[3], query[4], query[5]

        # 記事の存在をIDでチェック (未投稿or削除済み)
        if ArticleID not in Articles.keys() or (
            ArticleID in Articles.keys() and not Articles[ArticleID]["IsActive"]
        ):
            print("post_comment: article not found")

        # コメントIDがすでに使用されているかの確認
        elif CommentID in Comments.keys():
            print("post_comment: duplicated")

        # コメント投稿
        else:
            print(f"post_comment: {CommentID} {Context}")

            # 辞書に追加
            Comments[CommentID] = {
                "Datetime": Datetime,
                "UserID": UserID,
                "ArticleID": ArticleID,
                "Context": Context,
                "IsActive": True,  # コメントの存在フラグ
            }

            # 記事にコメントIDを追加
            Articles[ArticleID]["CommentIDs"].append(CommentID)

            # コメント履歴追加
            Users[UserID]["comment"].append((Datetime, CommentID))

    # コメント削除クエリ
    elif act == "delete_comment:":

        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[0] + " " + query[1], "%Y-%m-%d %H:%M:%S")
        UserID, CommentID = query[2], query[3]

        # コメントの存在をIDでチェック (未投稿or削除済み)
        if CommentID not in Comments.keys() or (
            CommentID in Comments.keys() and not Comments[CommentID]["IsActive"]
        ):
            print("delete_comment: not found")

        # ユーザIDが投稿ユーザIDと一致しているかを確認
        elif UserID != Comments[CommentID]["UserID"]:
            print("delete_comment: unauthorized")

        # コメント削除
        else:
            print(f"delete_comment: {CommentID} {Comments[CommentID]['Context']}")

            Comments[CommentID]["IsActive"] = False  # コメントの存在フラグを無効化

    # ユーザー情報表示クエリ
    elif act == "user:":
        UserID, kind = query[0], query[1]
        print(f"user: {UserID} {kind}")

        # 閲覧履歴の処理
        if kind == "view_history":

            tmp = []  # 出力用の一時配列
            tmp_st = set()  # 一時配列に含まれる記事IDのセット

            # 新しい履歴から確認を行う
            for time, article_id in reversed(Users[UserID]["view_history"]):

                # 削除されていないかつ出力に含まれない(重複しない)
                if Articles[article_id]["IsActive"] and article_id not in tmp_st:

                    # 出力用一時配列に追加
                    tmp.append((time, article_id))
                    tmp_st.add(article_id)

                    if len(tmp) >= 5:
                        break

            for i, (time, article_id) in enumerate(tmp):
                print(f"{i+1}. {article_id} {Articles[article_id]['Title']} ({time})")

        # コメント履歴の処理
        else:

            tmp = []  # 出力用の一時配列

            # 新しい履歴から確認を行う
            for time, comment_id in reversed(Users[UserID]["comment"]):

                # 記事削除されていないかつコメント削除されていない
                if (
                    Articles[Comments[comment_id]["ArticleID"]]["IsActive"]
                    and Comments[comment_id]["IsActive"]
                ):

                    # 出力用一時配列に追加
                    tmp.append((time, comment_id))

                    if len(tmp) >= 5:
                        break

            for i, (time, comment_id) in enumerate(tmp):
                print(
                    f"{i+1}. {comment_id} {Comments[comment_id]['Context']} ({time}, {Comments[comment_id]['ArticleID']})"
                )

    # ニュース記事一覧クエリ
    elif act == "list_article:":

        # Datetimeオブジェクトの作成
        Datetime = datetime.strptime(query[0] + " " + query[1], "%Y-%m-%d %H:%M:%S")
        kind = query[2]

        print(f"list_article: {kind}")

        # 閲覧数
        if kind == "views":
            tmp = []  # 出力用一時配列
            for key, value in Articles.items():  # 記事ごとのViewをカウント
                if value["IsActive"]:  # 記事の存在を確認
                    t = 0
                    for view in value["Views"]:
                        if Datetime - timedelta(days=30) <= view <= Datetime:
                            t += 1
                    tmp.append((key, t))
            tmp.sort(key=lambda x: (-x[1], x[0]))

            for i, (article_id, views) in enumerate(tmp[:5]):
                print(
                    f"{i+1}. {article_id} {Articles[article_id]['Title']} ({views} views)"
                )

        # コメント数
        elif kind == "most_comments":
            tmp = []  # 出力用一時配列
            for key, value in Articles.items():  # 記事ごとにコメントをカウント
                t = 0
                if value["IsActive"]:  # 記事の存在を確認
                    for comment_id in value["CommentIDs"]:
                        # 30 日以内かつコメントが有効かを確認
                        if (
                            Datetime - timedelta(days=30)
                            <= Comments[comment_id]["Datetime"]
                            <= Datetime
                        ) and Comments[comment_id]["IsActive"]:
                            t += 1
                    tmp.append((key, t))
            tmp.sort(
                key=lambda x: (-x[1], x[0])
            )  # 時間でソート 同IDは辞書で昇順にソート

            for i, (article_id, comments) in enumerate(tmp[:5]):
                print(
                    f"{i+1}. {article_id} {Articles[article_id]['Title']} ({comments} comments)"
                )

        # 投稿時刻
        else:
            tmp = []  # 出力用一時配列
            for key in Articles.keys():  # 記事ごとに時間を確認
                if Articles[key]["IsActive"]:
                    tmp.append((key, Articles[key]["Title"], Articles[key]["Datetime"]))

            tmp.sort(key=lambda x: x[2], reverse=True)  # 時間でソート

            for i, (article_id, title, date) in enumerate(tmp[:5]):
                print(f"{i+1}. {article_id} {Articles[article_id]['Title']} ({date})")

    # コメント一覧クエリ
    if act == "list_comment:":
        print("list_comment:")

        tmp = []  # 出力用一時配列
        for key in Comments.keys():
            if (
                Articles[Comments[key]["ArticleID"]]["IsActive"]
                and Comments[key]["IsActive"]
            ):
                tmp.append(
                    (
                        key,
                        Comments[key]["Context"],
                        Comments[key]["Datetime"],
                        Comments[key]["UserID"],
                        Comments[key]["ArticleID"],
                    )
                )

        tmp.sort(key=lambda x: x[2], reverse=True)  # 時間でソート

        for i, (comment_id, context, date, user_id, article_id) in enumerate(tmp[:5]):
            print(
                f"{i+1}. {comment_id} {context} ({date}, {user_id} commented on {article_id})"
            )
