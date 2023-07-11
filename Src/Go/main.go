package main

import (
	"fmt"

	"github.com/PuerkitoBio/goquery"
)

func main() {
	get_url_info, err := goquery.NewDocument("https://ip-ranges.amazonaws.com/ip-ranges.json")
	if err != nil {
		fmt.Println("get html NG")
	}

	result := get_url_info.Find("")
	result.Each(func(index int, s *goquery.Selection) {
		fmt.Println(s.Text())
	})
}
// 