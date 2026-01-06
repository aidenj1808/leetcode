class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        ret = set()
        for email in emails:
            local, domain = email.split("@")
            unique_local = local.split("+")[0].replace(".", "")
            ret.add(unique_local + "@" + domain)
        return len(ret)

