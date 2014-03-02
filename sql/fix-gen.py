import random

random.seed()

import datetime, time

# http://stackoverflow.com/a/553320/769384
def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d %H:%M:%S', prop)

#==============================================================================

DB_NAME = 'duck_database'
DB_TABLES = {
    'users': ['id', 'first_name', 'last_name', 'email_address', 'username', 'algorithm', 'salt', 'password', 'is_active', 'is_super_admin', 'last_login', 'created_at', 'updated_at'],
    'category': ['id', 'parent_id', 'name', 'type', 'created_at', 'updated_at', 'created_by', 'updated_by'],
    'income': ['id', 'category_id', 'amount', 'description', 'created_at', 'created_by'],
    'outcome': ['id', 'category_id', 'amount', 'description', 'created_at', 'created_by']
}
DB_ORDER = ['users', 'category', 'income', 'outcome']
DB_VALUES = {}

DB_VALUES['users'] = [
    (1, 'Paul', 'McCartney', 'paul.mccartney@beatles.com', 'pmc', 'sha1', '9137e482c18a1a9bb34ef7b992c79929', '2085e867458db5de8660402a0f50a8cf7d446235', 1, 1, '2011-10-18 19:22:27', '2011-10-18 19:22:27', '2011-10-18 19:22:27'),
    (2, 'John', 'Lennon', 'john.lennon@beatles.com', 'jl', 'sha1', '023b9c69a98e8bd0fa0960cf61ceb015', '8302ab7ba2febf30101dca94f046116652292f78', 1, 1, '2011-10-18 19:22:27', '2011-10-18 19:22:27', '2011-10-18 19:22:27'),
    (3, 'George', 'Harrison', 'george.harrison@beatles.com', 'gh', 'sha1', 'c69a961908e8bd0f960ceb015a03bcf2', '8302ab7ba2febf30101dca94f046116652292f78', 1, 1, '2011-10-18 19:22:27', '2011-10-18 19:22:27', '2011-10-18 19:22:27'),
    (4, 'Ringo', 'Starr', 'ringo.starr@beatles.com', 'rs', 'sha1', 'aa0fb90823158bde961ceb0960cf0c69', '8302ab7ba2febf30101dca94f046116652292f78', 1, 1, '2011-10-18 19:22:27', '2011-10-18 19:22:27', '2011-10-18 19:22:27')
]

DB_VALUES['category'] = [
    (1, None, 'food', 'outcome', '2011-10-18 19:22:27', '2011-10-18 19:22:27', 2, 2),
    (2, None, 'bills', 'outcome', '2011-10-18 19:22:27', '2011-10-18 19:22:27', 2, 2),
    (3, None, 'electronics', 'outcome', '2011-10-18 19:22:27', '2011-10-18 19:22:27', 2, 2),
    (4, None, 'entertainment', 'outcome', '2011-10-18 19:22:27', '2011-10-18 19:22:27', 2, 2),
    (5, None, 'transport', 'outcome', '2011-10-20 19:57:12', '2011-10-20 19:57:12', 2, 2),
    (6, None, 'hygiene', 'outcome', '2011-10-20 20:11:38', '2011-10-20 20:11:38', 2, 2),
    (7, None, 'house', 'outcome', '2011-10-20 20:17:47', '2011-10-20 20:17:47', 2, 2),
    (8, None, 'presents', 'outcome', '2011-10-20 20:42:31', '2011-10-20 20:42:31', 2, 2),
    (9, None, 'footwear', 'outcome', '2011-10-20 23:15:21', '2011-10-20 23:15:21', 2, 2),
    (10, None, 'clothing', 'outcome', '2011-10-20 23:15:25', '2011-10-20 23:15:25', 2, 2),
    (11, None, 'education', 'outcome', '2011-10-29 21:24:52', '2011-10-29 21:24:52', 2, 2),
    (12, None, 'health', 'outcome', '2012-03-23 10:48:39', '2012-03-23 10:48:39', 2, 2),
    (13, None, 'arms trade', 'income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
    (14, None, 'tribute', 'income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
    (15, None, 'music', 'income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
    (16, None, 'others', 'income', '2011-11-03 21:31:51', '2012-01-29 18:43:57', 2, 2),
    (17, None, 'investments', 'income', '2011-12-06 21:35:25', '2011-12-06 21:35:25', 2, 2),
    (18, 1, 'bread', 'outcome', '2011-10-20 19:05:00', '2011-10-20 19:05:00', 2, 2),
    (19, 1, 'fruits & vegs', 'outcome', '2011-10-20 19:20:17', '2011-10-22 05:36:49', 2, 2),
    (20, 1, 'lunch', 'outcome', '2011-10-20 19:57:34', '2011-10-20 19:57:48', 2, 2),
    (21, 1, 'meat', 'outcome', '2011-10-25 07:06:22', '2011-10-25 07:06:22', 2, 2),
    (22, 1, 'takeaway', 'outcome', '2011-10-25 17:38:05', '2011-10-25 17:40:11', 2, 2),
    (23, 1, 'alcohol', 'outcome', '2012-02-22 14:27:50', '2012-02-22 14:27:50', 2, 2),
    (24, 1, 'fish', 'outcome', '2012-05-06 12:06:30', '2012-05-06 12:06:30', 2, 2),
    (25, 2, 'rent', 'outcome', '2011-10-20 20:23:24', '2011-10-20 20:23:24', 2, 2),
    (26, 2, 'internet', 'outcome', '2011-10-20 20:26:56', '2011-10-20 20:26:56', 2, 2),
    (27, 2, 'water', 'outcome', '2011-10-23 17:42:56', '2011-10-23 17:42:56', 2, 2),
    (28, 2, 'gas', 'outcome', '2011-10-23 17:56:16', '2011-10-23 17:56:16', 2, 2),
    (29, 2, 'electricity', 'outcome', '2011-10-23 17:56:24', '2011-10-23 17:56:24', 2, 2),
    (30, 2, 'phones', 'outcome', '2011-10-23 17:56:33', '2011-10-23 17:56:33', 2, 2),
    (31, 4, 'cinema', 'outcome', '2011-10-20 21:17:05', '2011-10-20 21:17:05', 2, 2),
    (32, 4, 'theatre', 'outcome', '2012-01-26 17:40:57', '2012-01-26 17:40:57', 2, 2),
    (33, 4, 'collectibles', 'outcome', '2012-03-29 13:10:24', '2012-03-29 13:10:24', 2, 2),
    (34, 4, 'travels', 'outcome', '2011-10-18 19:22:27', '2011-10-20 20:52:21', 2, 2),
    (35, 4, 'books', 'outcome', '2011-10-20 20:08:46', '2011-10-20 20:08:46', 2, 2),
    (36, 4, 'bar', 'outcome', '2011-10-20 19:20:08', '2011-10-20 19:20:08', 2, 2),
    (37, 4, 'press', 'outcome', '2011-10-20 19:56:56', '2011-10-20 20:52:04', 2, 2),
    (38, 6, 'cosmetics', 'outcome', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
    (39, 6, 'barber', 'outcome', '2012-03-06 23:55:17', '2012-03-06 23:55:17', 1, 1),
    (40, 7, 'repairs', 'outcome', '2011-10-20 20:30:48', '2011-10-20 20:30:48', 2, 2),
    (41, 7, 'tools', 'outcome', '2011-10-20 20:51:23', '2011-10-20 20:51:23', 2, 2),
    (42, 7, 'flowers', 'outcome', '2011-10-23 17:45:39', '2011-10-23 17:45:39', 2, 2),
    (43, 7, 'chemistry', 'outcome', '2011-10-20 20:10:26', '2011-10-20 20:10:26', 2, 2),
    (44, 7, 'household goods', 'outcome', '2011-10-20 20:16:25', '2012-09-09 14:04:58', 2, 1),
    (45, 8, 'handout', 'outcome', '2012-05-13 19:10:11', '2012-05-13 19:10:11', 2, 2),
    (46, 8, 'souvenirs', 'outcome', '2012-08-17 10:36:07', '2012-08-17 10:36:07', 2, 2),
    (47, 12, 'doctor', 'outcome', '2012-03-23 10:48:51', '2012-03-23 10:48:51', 2, 2),
    (48, 12, 'meds', 'outcome', '2011-10-25 07:00:33', '2012-03-23 10:49:06', 2, 2),
    (49, 13, 'trips', 'income', '2011-10-26 17:44:22', '2012-01-29 18:44:07', 2, 2),
    (50, 13, 'production', 'income', '2012-01-29 18:41:46', '2012-01-29 18:41:46', 2, 2),
    (51, 15, 'recordings', 'income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
    (52, 15, 'live shows', 'income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
    (53, 17, 'gold & silver', 'income', '2011-12-06 21:35:39', '2011-12-06 21:35:39', 2, 2),
    (54, 17, 'debentures', 'income', '2012-01-02 14:34:32', '2012-01-02 14:34:32', 2, 2),
    (55, 17, 'real estate', 'income', '2012-05-25 15:10:21', '2012-05-25 15:10:21', 2, 2)
]

income_categories = [row for row in DB_VALUES['category'] if row[3] == 'income']
outcome_categories = [row for row in DB_VALUES['category'] if row[3] == 'outcome']

income_count = random.randint(1000, 2000)
outcome_count = random.randint(5000, 7000)

now = datetime.datetime(2009,5,5)
str_now = now.date().isoformat()

DB_VALUES['income'] = [(
    _id,
    random.choice(income_categories)[0],
    random.uniform(random.randint(100, 200), random.randint(100, 1000) * 2),
    None,
    randomDate("2000-1-1 00:00:00", "2013-12-31 23:59:59", random.random()),
    random.choice(DB_VALUES['users'])[0]
) for _id in range(1, income_count)]

DB_VALUES['outcome'] = [(
    _id,
    random.choice(income_categories)[0],
    random.uniform(random.randint(10, 200), random.randint(100, 500)),
    None,
    randomDate("2000-1-1 00:00:00", "2013-12-31 23:59:59", random.random()),
    random.choice(DB_VALUES['users'])[0]
) for _id in range(1, outcome_count)]

content = 'USE `%s`;\n\n' % (DB_NAME,)
for table in DB_ORDER:
    fields = ', '.join('`%s`' % (field) for field in DB_TABLES[table])
    values = []
    for row in DB_VALUES[table]:
        row = ('\'' + str(cell) + '\'' if cell else 'NULL' for cell in row)
        values.append('(' + ', '.join(row) + ')')
    values = ',\n'.join(values)
    content += 'INSERT INTO `%s` (%s) VALUES\n%s;\n\n' % (table, fields, values)

f = open('fixtures.sql', 'w')
f.write(content)
f.close()
