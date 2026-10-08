# Database Design

```mermaid
erDiagram
roles ||--o{ users : "role"
ranks ||--o{ users : "current_rank"
users ||--o| user_details : "user_id"
vessels ||--o{ drills : "vessel_id"
drill_types ||--o{ drill_names : "type_id"
drill_names ||--o{ drills : "drill_name_id"
drills ||--o{ drill_attendance : "drill_id"
users ||--o{ drill_attendance : "user_id"
ranks ||--o{ drill_attendance : "rank_id"

users {
integer id PK "identity"
text title
text first_name
text family_name
text email UK
text password_hash
text status
integer role FK "roles.id"
integer current_rank FK "ranks.id"
}
user_details {
integer id PK "identity"
text address
text postcode
text gender
integer user_id FK,UK "users.id"
}
roles {
integer id PK "identity"
text name UK
bool is_admin "default false"
}
ranks {
integer id PK "identity"
text name UK
}
vessels {
integer id PK "identity"
text name UK
text image_path
}
drill_types {
integer id PK "identity"
text name UK "Drill or Training"
}
drill_names {
integer id PK "identity"
smallint sort_order
text name UK
integer type_id FK "drill_types.id"
}
drills {
integer id PK "identity"
integer drill_name_id FK "drill_names.id"
date conducted_on
text comments
integer vessel_id FK "vessels.id"
}
drill_attendance {
integer id PK "identity"
integer drill_id FK "drills.id — unique with user_id"
integer user_id FK "users.id"
integer rank_id FK "ranks.id"
}
```

`drill_attendance` has a composite `UNIQUE (drill_id, user_id)` so a person can only be recorded once per drill.

## Tables

| Table            | Purpose                                                | Key fields                                          |
| ---------------- | ------------------------------------------------------ | --------------------------------------------------- |
| users            | Crew and staff                                         | role → roles, current_rank → ranks                  |
| user_details     | Personal details, one row per user                     | user_id → users                                     |
| roles            | User roles                                             |                                                     |
| ranks            | Shipboard ranks                                        |                                                     |
| vessels          | Ships                                                  |                                                     |
| drill_types      | Drill (practical) or Training (classroom)              |                                                     |
| drill_names      | Each drill or course (Fire, Abandon Ship, ...)         | type_id → drill_types                               |
| drills           | A drill or training session held on a vessel on a date | drill_name_id → drill_names, vessel_id → vessels    |
| drill_attendance | Who attended each drill, at the rank they held then    | drill_id → drills, user_id → users, rank_id → ranks |
