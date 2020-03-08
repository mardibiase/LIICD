from typing import List
from index import IndexEntry


class IndexEntriesGroup:

    def __init__(self, index_entries=None):
        if index_entries is None:
            index_entries = []
        self.index_entries_group = index_entries

    def __str__(self):
        to_ret = ""
        for index_entry in self.index_entries_group:
            to_ret += str(index_entry) + "\n"
        return to_ret

    def get__index_entries_group(self):
        return self.index_entries_group

    def get__size(self):
        return len(self.index_entries_group)

    def add_entry(self, index_entry):
        self.index_entries_group.append(index_entry)

    def extend(self, index_entries_to_append):
        self.index_entries_group.extend(index_entries_to_append)

    def subset_of(self, prev_group, index_correction=1):
        i = 0
        j = 0
        current_group = self.index_entries_group

        while i < len(current_group) and j < len(prev_group):
            current_group_entry = current_group[i]
            previous_group_entry = prev_group[j]
            current_group_entry_filename = current_group_entry.get__file_name()
            previous_group_entry_filename = previous_group_entry.get__file_name()

            if current_group_entry_filename != previous_group_entry_filename:
                j += 1
                continue

            idx = current_group_entry.get__statement_index() - index_correction - previous_group_entry.get__statement_index()

            if idx < 0:
                break
            if idx != 0:
                j += 1
            else:
                j += 1
                i += 1

        return i == len(current_group)
