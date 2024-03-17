# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  treeUtil.py
@Description    :  列表组装为树状结构数据
@CreateTime     :  2024/03/12
------------------------------------
"""


class ListToTreeUtil:
    def __init__(self, node_id, parent_id, root_value=None):
        """

        :param node_id: 节点的key
        :param parent_id: 判断字节的的key
        :param root_value: 根节点的value
        示例：
        [{id:1, parent_id: None}, {id:2, parent_id: 2}]
        ListToTreeUtil('id', 'parent_id', 'None')
        """
        self.root = []
        self.node = []

        self.node_id = node_id
        self.parent_id = parent_id
        self.root_value = root_value

    def list_to_tree(self, list_data: list[dict]):
        """
        将list组装为 tree数据
        :param list_data:
        :return:
        """
        for data in list_data:
            data['choice'] = 0
            if data.get(self.parent_id) == self.root_value:
                self.root.append(data)
            else:
                self.node.append(data)
        # 查找子节点
        for p in self.root:
            self.add_node(p, self.node)

        # 无子节点
        if len(self.root) == 0:
            return self.node

        return self.root

    def add_node(self, root_node, node_data):
        """
        子节点list
        :return:
        """
        root_node["children"] = []
        for node in node_data:
            if node.get(self.parent_id) == root_node.get(self.node_id):
                root_node["children"].append(node)
                root_node['choice'] += 1

        # 递归子节点，查找子节点的节点
        for root_n in root_node["children"]:
            if not root_n.get("children"):
                root_n["children"] = []
            root_n["children"].append(self.add_node(root_n, node_data))

        # 退出递归的条件
        if len(root_node["children"]) == 0:
            root_node.pop("children")
            root_node.pop("choice")
            return


if __name__ == "__main__":
    pass
