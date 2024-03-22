from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_freq = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            subdomains = self.process_domain(domain)

            for subdomain in subdomains:
                domain_freq[subdomain] += count

        result = []
        for subdomain, freq in domain_freq.items():
            result.append(f"{freq} {subdomain}")

        return result

    def process_domain(self, domain: str) -> List[str]:
        res = []
        split_domain = domain.split(".")
        for i in range(len(split_domain)):
            sub_domain = ".".join(split_domain[i:])
            res.append(sub_domain)
        return res
