import yaml


class TestYaml:
    #一维数组
    # - Hesperiidae
    # - Papilionidae
    # - Apatelodidae
    # - Epiplemidae
    #输出：['Hesperiidae', 'Papilionidae', 'Apatelodidae', 'Epiplemidae']
    #如下是二维数组
    def test_yaml(self):
        print(yaml.load("""
    -
        - 1
        - 2
        - 3
    -
        - 4
        - 5
        - 6   
        """))

    # @pytest.mark.parametrize("key, stock_type, price", [
    #     ("alibaba", "BABA", 200),
    #     ("JD", "JD", 20)
    # ])
    def test_yaml_zhidian(self):
        print(yaml.safe_load(open("test.yaml")))
