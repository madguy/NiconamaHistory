#-*- coding:utf-8

from niconama_history.plugin_base import PluginBase

class CommentFilter(PluginBase):
    """
    常連さんの出現を抽出するプラグインです。
    """
    def ready(self, db):
        sql = """
            SELECT
                user_id
                ,name
            FROM
                comment
            WHERE
                name IS NOT NULL
            GROUP BY
                user_id
                ,name
            HAVING
                count(user_id) > {0}
            ;
        """.format(1000)
        self.regularSet = set(db.connect.execute(sql).fetchall())

    def analyzeDay(self, date, rows):
        messages = []
        for row in rows:
            ragulars = filter(lambda (userId, name): userId == row.userId, self.regularSet)
            if len(ragulars) > 0:
                self.regularSet -= set(ragulars)
                messages.extend(map(lambda (userId, name): u'{0}が初登場'.format(name), ragulars))

        return messages

if __name__ == '__main__':
    pass
