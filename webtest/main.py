from datetime import datetime, timedelta


class NewsSys:
    def __init__(self):

        self.Articles = {}  # 記事dict
        """
        key: ArticleID
        - "Datetime" : Datetimeオブジェクト
        - "UserID": 記事を投稿したユーザーのID
        - "Title": 記事のタイトル
        - "CommentIDs": コメントIDを保持する配列
        - "IsActive": 記事が現在アクティブかどうかを示すbool
        """

        self.Comments = {}  # コメントデータdict
        """
        key: CommentID
        - "Datetime" : Datetimeオブジェクト
        - "UserID": コメントを投稿したユーザーのID
        - "ArticleID": 記事のID
        - "Context": コメント本文
        - "IsActive": True,  # コメントが現在アクティブかどうかを示すbool
        """

        self.Users = {}  # ユーザーデータdict
        """
        key: UserID
        - "view_history": 閲覧した記事IDを保持する配列 (ID, 時刻)
        - "comment": コメントIDの履歴を保持する配列
        - "permission": ユーザーの権限を示すbool
        """

    # ユーザー追加
    def add_user(self, user_id, permission):

        # ユーザー追加
        self.Users[user_id] = {
            "view_history": [],
            "comment": [],
            "permission": True if permission == "1" else False,
        }

    # タイムスタンプ変換
    def convert_to_timestamp(self, date, time):
        timestamp = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M:%S")
        return timestamp

    # クエリ振り分け
    def process_query(self, act, *query):

        # 記事投稿
        if act == "post_article:":
            # 引数変換
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, article_id, title = query[2], query[3], query[4]
            # 記事投稿関数呼び出し
            self.post_article(timestamp, user_id, article_id, title)

        # 記事削除
        elif act == "delete_article:":
            # 引数変換
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, article_id = query[2], query[3]
            # 記事削除関数呼び出し
            self.delete_article(timestamp, user_id, article_id)

        # 記事閲覧
        elif act == "view_article:":
            # 引数変換
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, article_id = query[2], query[3]
            # 記事閲覧関数呼び出し
            self.view_article(timestamp, user_id, article_id)

        # コメント投稿
        elif act == "post_comment:":
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, article_id = query[2], query[3]
            comment_id, body = query[4], query[5]
            # コメント投稿関数呼び出し
            self.post_comment(timestamp, user_id, article_id, comment_id, body)

        # コメント削除
        elif act == "delete_comment:":
            # 引数変換
            timestamp = self.convert_to_timestamp(query[0], query[1])
            user_id, comment_id = query[2], query[3]
            # コメント削除関数呼び出し
            self.delete_comment(timestamp, user_id, comment_id)

        # ユーザー情報表示
        elif act == "user:":
            # 引数変換
            user_id, kind = query[0], query[1]
            print(f"user: {user_id} {kind}")
            # ユーザー情報表示関数呼び出し
            self.show_user_info(user_id, kind)

        # 記事一覧表示
        elif act == "list_article:":
            # 引数変換
            timestamp = self.convert_to_timestamp(query[0], query[1])
            kind = query[2]
            print(f"list_article: {kind}")
            # 記事一覧行事関数呼び出し
            self.list_articles(timestamp, kind)

        # コメント一覧クエリ
        elif act == "list_comment:":
            print("list_comment:")
            # コメント一覧関数呼び出し
            self.list_comment()

        # 例外処理
        else:
            raise Exception("process_query error")

    # 記事投稿処理
    def post_article(self, timestamp, user_id, article_id, title):

        # ユーザーが権限を有しているかのチェック
        if not self.Users[user_id]["permission"]:
            print("post_article: unauthorized")

        # 記事がすでに投稿されているかの確認
        elif article_id in self.Articles.keys():
            print("post_article: duplicated")

        # 記事投稿
        else:
            # 辞書に追加
            self.Articles[article_id] = {
                "Datetime": timestamp,
                "UserID": user_id,
                "Title": title,
                "CommentIDs": [],  # コメントのIDリスト
                "Views": [],  # 閲覧履歴（Datetimeで管理）
                "IsActive": True,  # 記事の存在フラグ
            }

            print(f"post_article: {article_id} {title}")

    # 記事削除処理
    def delete_article(self, timestamp, user_id, article_id):

        # 記事の存在をチェック
        if article_id not in self.Articles.keys() or (
            article_id in self.Articles.keys()
            and not self.Articles[article_id]["IsActive"]
        ):
            print("delete_article: not found")

        # ユーザーIDが記事作者と一致するかチェック
        elif user_id != self.Articles[article_id]["UserID"]:
            print("delete_article: unauthorized")

        # 記事削除
        else:
            # 有効コメント数を取得
            comments_count = sum(
                1
                for CommentID in self.Articles[article_id]["CommentIDs"]
                if self.Comments[CommentID]["IsActive"]
            )

            # 記事内コメントも削除
            for CommentID in self.Articles[article_id]["CommentIDs"]:
                self.Comments[CommentID]["IsActive"] = False

            print(f"delete_article: {article_id} {comments_count}")
            self.Articles[article_id]["IsActive"] = False  # 記事の存在フラグを無効化

    # 記事閲覧処理
    def view_article(self, timestamp, user_id, article_id):
        # 記事の存在をIDでチェック (未投稿or削除済み)
        if article_id not in self.Articles.keys() or (
            article_id in self.Articles.keys()
            and not self.Articles[article_id]["IsActive"]
        ):
            print("view_article: not found")

        # 記事閲覧
        else:
            print(f"view_article: {user_id} {article_id}")

            # 閲覧履歴追加
            self.Users[user_id]["view_history"].append((timestamp, article_id))
            self.Articles[article_id]["Views"].append(timestamp)

    # コメント投稿処理
    def post_comment(self, timestamp, user_id, article_id, comment_id, body):
        # 記事の存在をIDでチェック (未投稿or削除済み)
        if article_id not in self.Articles.keys() or (
            article_id in self.Articles.keys()
            and not self.Articles[article_id]["IsActive"]
        ):
            print("post_comment: article not found")

        # コメントIDがすでに使用されているかの確認
        elif comment_id in self.Comments.keys():
            print("post_comment: duplicated")

        # コメント投稿
        else:
            print(f"post_comment: {comment_id} {body}")

            # 辞書に追加
            self.Comments[comment_id] = {
                "Datetime": timestamp,
                "UserID": user_id,
                "ArticleID": article_id,
                "Context": body,
                "IsActive": True,  # コメントの存在フラグ
            }

            # 記事にコメントIDを追加
            self.Articles[article_id]["CommentIDs"].append(comment_id)

            # コメント履歴追加
            self.Users[user_id]["comment"].append((timestamp, comment_id))

    # コメント削除処理
    def delete_comment(self, timestamp, user_id, comment_id):
        # コメントの存在をIDでチェック (未投稿or削除済み)
        if comment_id not in self.Comments.keys() or (
            comment_id in self.Comments.keys()
            and not self.Comments[comment_id]["IsActive"]
        ):
            print("delete_comment: not found")

        # ユーザIDが投稿ユーザIDと一致しているかを確認
        elif user_id != self.Comments[comment_id]["UserID"]:
            print("delete_comment: unauthorized")

        # コメント削除
        else:
            print(
                f"delete_comment: {comment_id} {self.Comments[comment_id]['Context']}"
            )

            self.Comments[comment_id][
                "IsActive"
            ] = False  # コメントの存在フラグを無効化

    # ユーザー情報表示処理
    def show_user_info(self, user_id, kind):
        # 閲覧履歴の処理
        if kind == "view_history":

            tmp = []  # 出力用の一時配列
            tmp_st = set()  # 一時配列に含まれる記事IDのセット

            # 新しい履歴から確認を行う
            for time, article_id in reversed(self.Users[user_id]["view_history"]):

                # 削除されていないかつ出力に含まれない(重複しない)
                if self.Articles[article_id]["IsActive"] and article_id not in tmp_st:

                    # 出力用一時配列に追加
                    tmp.append((time, article_id))
                    tmp_st.add(article_id)

                    if len(tmp) >= 5:
                        break

            for i, (time, article_id) in enumerate(tmp):
                print(
                    f"{i+1}. {article_id} {self.Articles[article_id]['Title']} ({time})"
                )

        # コメント履歴の処理
        else:

            tmp = []  # 出力用の一時配列

            # 新しい履歴から確認を行う
            for time, comment_id in reversed(self.Users[user_id]["comment"]):

                # 記事削除されていないかつコメント削除されていない
                if (
                    self.Articles[self.Comments[comment_id]["ArticleID"]]["IsActive"]
                    and self.Comments[comment_id]["IsActive"]
                ):

                    # 出力用一時配列に追加
                    tmp.append((time, comment_id))

                    if len(tmp) >= 5:
                        break

            for i, (time, comment_id) in enumerate(tmp):
                print(
                    f"{i+1}. {comment_id} {self.Comments[comment_id]['Context']} ({time}, {self.Comments[comment_id]['ArticleID']})"
                )

    # 記事一覧表示処理
    def list_articles(self, timestamp, kind):
        # 閲覧数
        if kind == "views":
            tmp = []  # 出力用一時配列
            for key, value in self.Articles.items():  # 記事ごとのViewをカウント
                if value["IsActive"]:  # 記事の存在を確認
                    t = 0
                    for view in value["Views"]:
                        if timestamp - timedelta(days=30) <= view <= timestamp:
                            t += 1
                    tmp.append((key, t))
            tmp.sort(key=lambda x: (-x[1], x[0]))

            for i, (article_id, views) in enumerate(tmp[:5]):
                print(
                    f"{i+1}. {article_id} {self.Articles[article_id]['Title']} ({views} views)"
                )

        # コメント数
        elif kind == "most_comments":
            tmp = []  # 出力用一時配列
            for key, value in self.Articles.items():  # 記事ごとにコメントをカウント
                t = 0
                if value["IsActive"]:  # 記事の存在を確認
                    for comment_id in value["CommentIDs"]:
                        # 30 日以内かつコメントが有効かを確認
                        if (
                            timestamp - timedelta(days=30)
                            <= self.Comments[comment_id]["Datetime"]
                            <= timestamp
                        ) and self.Comments[comment_id]["IsActive"]:
                            t += 1
                    tmp.append((key, t))
            tmp.sort(
                key=lambda x: (-x[1], x[0])
            )  # 時間でソート 同IDは辞書で昇順にソート

            for i, (article_id, comments) in enumerate(tmp[:5]):
                print(
                    f"{i+1}. {article_id} {self.Articles[article_id]['Title']} ({comments} comments)"
                )

        # 投稿時刻
        else:
            tmp = []  # 出力用一時配列
            for key in self.Articles.keys():  # 記事ごとに時間を確認
                if self.Articles[key]["IsActive"]:
                    tmp.append(
                        (
                            key,
                            self.Articles[key]["Title"],
                            self.Articles[key]["Datetime"],
                        )
                    )

            tmp.sort(key=lambda x: x[2], reverse=True)  # 時間でソート

            for i, (article_id, title, date) in enumerate(tmp[:5]):
                print(f"{i+1}. {article_id} {title} ({date})")

    # コメント一覧表示処理
    def list_comment(self):
        tmp = []  # 出力用一時配列
        for key in self.Comments.keys():
            if (
                self.Articles[self.Comments[key]["ArticleID"]]["IsActive"]
                and self.Comments[key]["IsActive"]
            ):
                tmp.append(
                    (
                        key,
                        self.Comments[key]["Context"],
                        self.Comments[key]["Datetime"],
                        self.Comments[key]["UserID"],
                        self.Comments[key]["ArticleID"],
                    )
                )

        tmp.sort(key=lambda x: x[2], reverse=True)  # 時間でソート

        for i, (comment_id, context, date, user_id, article_id) in enumerate(tmp[:5]):
            print(
                f"{i+1}. {comment_id} {context} ({date}, {user_id} commented on {article_id})"
            )


def main():

    system = NewsSys()

    # ユーザー追加
    n = int(input())
    for _ in range(n):
        UserID, Permission = input().split()
        system.add_user(UserID, Permission)

    # クエリ処理
    m = int(input())
    q = [list(input().split()) for _ in range(m)]
    for act, *query in q:
        system.process_query(act, *query)


if __name__ == "__main__":
    main()
