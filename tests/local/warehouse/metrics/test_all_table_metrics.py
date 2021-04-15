#  Copyright 2020 Soda
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from sodasql.scan.metric import Metric
from sodasql.scan.scan_yml_parser import KEY_METRIC_GROUPS
from tests.common.sql_test_case import SqlTestCase


class TestAllTableMetrics(SqlTestCase):

    def test_all_metric_groups(self):
        self.sql_recreate_table(
            [f"score {self.dialect.data_type_varchar_255}"],
            ["('1')",
             "('2')",
             "('2')",
             "('3')",
             "('3')",
             "('3')",
             "('3')",
             "('3')",
             "('4')",
             "('4')",
             "('5')",
             "(null)"])

        scan_result = self.scan({
            KEY_METRIC_GROUPS: [
                Metric.METRIC_GROUP_ALL
            ]
        })

        self.assertEqual(scan_result.get(Metric.INVALID_COUNT), 12)
