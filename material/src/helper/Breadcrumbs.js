import React from 'react';
import Breadcrumbs from "@material-ui/core/Breadcrumbs";
import Typography from "@material-ui/core/Typography";
import Link from "@material-ui/core/Link";

export function getNavigation(name) {
    let navigation = {
        'login': [
            {label: 'Главная', url:'/'},
            {label: 'Авторизация'},
        ],
        'profile': [
            {label: 'Главная', url: '/'},
            {label: 'Настройки'},
        ]

    };
    return navigation[name]
}

export default function PageBreadcrumbs({navigation = []}) {
    const render_link = (item, index) => {
        return item.url ? <Link color="inherit" href={item.url} key={index}>
            {item.label}
        </Link> :
            <Typography>
                {item.label}
            </Typography>
    };
    return (
        <Breadcrumbs maxItems={2} aria-label="breadcrumb">
            {navigation.map((item, index) =>  render_link(item, index))}
        </Breadcrumbs>
    )
}