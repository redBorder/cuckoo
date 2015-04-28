import os

from lib.cuckoo.common.exceptions import CuckooReportError
from lib.cuckoo.common.abstracts import Report

class HdfsUpload(Report):
    """Saves analysis results in HDFS node when the proccess has been finished"""

    def run(self, results):
        try:
            if os.system("hdfs dfs -test -e hdfs://hadoopnamenode.redborder.cluster:8020/user/cuckoo/"):
                    os.system("hdfs dfs -mkdir hdfs://hadoopnamenode.redborder.cluster:8020/user/cuckoo")
            path = str(self.analysis_path)
            os.system("hdfs dfs -put %s hdfs://hadoopnamenode.redborder.cluster:8020/user/cuckoo/" % path)
        except (UnicodeError, TypeError, IOError) as e:
            raise CuckooReportError("Failed to generate HDFSUpload report: %s" % e)
