package main

import (
	"fmt"

	"github.com/PuerkitoBio/goquery"
)

func main() {
	get_url_info, err := goquery.NewDocument("検索したいURL")
	if err != nil {
		fmt.Println("get html NG")
	}

	result := get_url_info.Find("")
	result.Each(func(index int, s *goquery.Selection) {
		fmt.Println(s.Text())
	})
}